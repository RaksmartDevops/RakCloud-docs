#!/usr/bin/env bash
# 定时拉取 dist 分支：发现新版本就落地到 releases/<sha>/，并把 staging 软链接切过去。
# 只更新 staging，不碰 production；晋升由 promote.sh 人工执行。
set -euo pipefail

REPO_URL="${REPO_URL:-https://github.com/RaksmartDevops/RakCloud-docs.git}"
DIST_BRANCH="${DIST_BRANCH:-dist}"
WWW_ROOT="${WWW_ROOT:-/var/www}"
KEEP_RELEASES="${KEEP_RELEASES:-5}"
SHA_LEN=12
# 网络连接可能僵死不返回，git 命令超过该秒数就放弃，等下个周期重试
GIT_TIMEOUT_SECS="${GIT_TIMEOUT_SECS:-120}"
# 构建产物中必须存在的文件，缺任何一个都视为坏版本，不上线
REQUIRED_FILES=(index.html 404.html sitemap.xml BUILD_INFO)

RELEASES_DIR="$WWW_ROOT/releases"
STAGING_LINK="$WWW_ROOT/staging"
PRODUCTION_LINK="$WWW_ROOT/production"
LOCK_FILE="$WWW_ROOT/.pull-dist.lock"

log() { echo "[$(date '+%F %T')] $*"; }

mkdir -p "$RELEASES_DIR"

# 防止上一次拉取未结束时重复执行
exec 9>"$LOCK_FILE"
flock -n 9 || { log "已有拉取任务在运行，跳过"; exit 0; }

# 原子切换软链接：先建临时链接再 rename，避免 Nginx 读到不存在的中间状态
switch_link() {
  local target="$1" link="$2"
  ln -s "$target" "$link.tmp"
  mv -T "$link.tmp" "$link"
}

# 清理上次异常中断遗留的半成品（已持有锁，不会误删正在下载的目录）
rm -rf "$RELEASES_DIR"/.tmp-*

remote_sha="$(timeout "$GIT_TIMEOUT_SECS" git ls-remote "$REPO_URL" "refs/heads/$DIST_BRANCH" | cut -f1)"
if [[ -z "$remote_sha" ]]; then
  log "错误：远程没有 $DIST_BRANCH 分支，或无法访问 $REPO_URL"
  exit 1
fi
release_name="${remote_sha:0:SHA_LEN}"
release_dir="$RELEASES_DIR/$release_name"

if [[ -d "$release_dir" ]]; then
  log "版本 $release_name 已存在，无需下载"
else
  tmp_dir="$RELEASES_DIR/.tmp-$release_name"
  rm -rf "$tmp_dir"
  # 失败时清理半成品，保证 releases/ 下只有完整版本
  trap 'rm -rf "$tmp_dir"' EXIT

  log "下载 $DIST_BRANCH @ $release_name"
  timeout "$GIT_TIMEOUT_SECS" git clone --quiet --depth 1 --branch "$DIST_BRANCH" "$REPO_URL" "$tmp_dir"

  for f in "${REQUIRED_FILES[@]}"; do
    if [[ ! -f "$tmp_dir/$f" ]]; then
      log "错误：产物缺少 $f，放弃此版本"
      exit 1
    fi
  done

  rm -rf "$tmp_dir/.git"
  mv -T "$tmp_dir" "$release_dir"
  trap - EXIT
fi

current_staging="$(readlink "$STAGING_LINK" 2>/dev/null || true)"
if [[ "$current_staging" == "$release_dir" ]]; then
  log "staging 已指向 $release_name"
else
  switch_link "$release_dir" "$STAGING_LINK"
  log "staging 已切换到 $release_name（$(grep '^commit=' "$release_dir/BUILD_INFO" || true)）"
fi

# 清理旧版本：保留最新 KEEP_RELEASES 个，且永远不删 staging / production 正在使用的
in_use=("$(readlink "$STAGING_LINK" 2>/dev/null || true)" "$(readlink "$PRODUCTION_LINK" 2>/dev/null || true)")
mapfile -t all_releases < <(find "$RELEASES_DIR" -mindepth 1 -maxdepth 1 -type d ! -name '.tmp-*' -printf '%T@ %p\n' | sort -rn | cut -d' ' -f2-)
index=0
for dir in "${all_releases[@]}"; do
  index=$((index + 1))
  (( index <= KEEP_RELEASES )) && continue
  if [[ " ${in_use[*]} " == *" $dir "* ]]; then
    continue
  fi
  log "清理旧版本 $(basename "$dir")"
  rm -rf "$dir"
done

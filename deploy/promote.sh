#!/usr/bin/env bash
# 晋升：把 production 软链接指向指定版本，默认为 staging 当前版本。
# 用法：
#   promote.sh            # 晋升 staging 当前验证过的版本
#   promote.sh <版本名>    # 指定版本（用于回滚到 releases/ 下的旧版本）
#   promote.sh --list     # 列出可用版本及 staging / production 现状
set -euo pipefail

WWW_ROOT="${WWW_ROOT:-/var/www}"
RELEASES_DIR="$WWW_ROOT/releases"
STAGING_LINK="$WWW_ROOT/staging"
PRODUCTION_LINK="$WWW_ROOT/production"

log() { echo "[$(date '+%F %T')] $*"; }

link_name() { basename "$(readlink "$1" 2>/dev/null || echo '-')"; }

list_releases() {
  echo "staging:    $(link_name "$STAGING_LINK")"
  echo "production: $(link_name "$PRODUCTION_LINK")"
  echo "可用版本（新到旧）："
  find "$RELEASES_DIR" -mindepth 1 -maxdepth 1 -type d ! -name '.tmp-*' -printf '%T@ %f\n' | sort -rn | cut -d' ' -f2- | sed 's/^/  /'
}

if [[ "${1:-}" == "--list" ]]; then
  list_releases
  exit 0
fi

if [[ -n "${1:-}" ]]; then
  target_name="$1"
else
  if [[ ! -L "$STAGING_LINK" ]]; then
    log "错误：staging 尚未就绪，请先运行 pull-dist.sh"
    exit 1
  fi
  target_name="$(link_name "$STAGING_LINK")"
fi

# 只接受 releases/ 下的目录名，防止路径穿越
if [[ "$target_name" == */* || "$target_name" == .* ]]; then
  log "错误：版本名不合法：$target_name"
  exit 1
fi
target_dir="$RELEASES_DIR/$target_name"
if [[ ! -f "$target_dir/index.html" ]]; then
  log "错误：版本 $target_name 不存在或不完整"
  list_releases
  exit 1
fi

previous="$(link_name "$PRODUCTION_LINK")"
if [[ "$previous" == "$target_name" ]]; then
  log "production 已经是 $target_name，无需操作"
  exit 0
fi

# 相对路径链接，宿主机与 Nginx 容器内均可解析
ln -s "releases/$target_name" "$PRODUCTION_LINK.tmp"
mv -T "$PRODUCTION_LINK.tmp" "$PRODUCTION_LINK"
log "production: $previous -> $target_name"
if [[ "$previous" != "-" ]]; then
  log "如需回滚：promote.sh $previous"
fi

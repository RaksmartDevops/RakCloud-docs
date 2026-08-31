# Centos8 无法使用Yum及Dnf

1.导致原因：CentOS 8：2021年底停止更新

2.问题报错图：

![](./images/2a123b47f7848ecc.png)

3.报错关键词：

Failed to synchronize cache for repo 'AppStream', ignoring this repo.

注释：无法同步 repo 'AppStream' 的缓存，忽略此 repo
Failed to synchronize cache for repo 'BaseOS', ignoring this repo.

注释：无法同步 repo 'BaseOS' 的缓存，忽略此 repo。

Last metadata expiration check: 0:45:16 ago on Thu Jul 7 19:20:18 2022.

注释：上次元数据过期检查：2022 年 7 月 7 日星期四 19:20:18 前 0:45:16。
No match for argument: wget

注释：参数不匹配:wget
Error: Unable to find a match

注释：错误:无法找到匹配

4.解决方法：

sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-\*

sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-\*

依次执行调整后执行Dnf或Yum即可正常使用。

注释：要修复上述错误，我们需要使用以下命令将指向 CentOS 官方 URL 的 repo URL 更改為 [vault.centos.org](https://vault.centos.org/ "https://vault.centos.org/")

以上如果不好使用以下命令(阿里云的镜像)

curl -o /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-vault-8.5.2111.repo

yum makecache

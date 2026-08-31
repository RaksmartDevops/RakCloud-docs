# How to switch to a different repository for CentOS 8 EOL

CentOS 8 reached its end of life at the end of 2021. When using yum repositories for installation, you may encounter the following error:

![](./images/a9aeb16e40ec0ef0.png)

Solution:

1、Navigate to the "repos" directory of yum.

cd /etc/yum.repos.d/

2、Modify the contents of all CentOS files.

sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-\*

sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-\*

3、Update the yum source to Alibaba Mirror.

yum clean all && yum makecache

yum -y install wget

wget -O /etc/yum.repos.d/CentOS-Base.repo <https://mirrors.aliyun.com/repo/Centos-vault-8.5.2111.repo>

yum -y install epel-release

After switching to the Alibaba Mirror, test if you can successfully use yum to download the desired tools.

![](./images/5891fffabedd0b4f.png)

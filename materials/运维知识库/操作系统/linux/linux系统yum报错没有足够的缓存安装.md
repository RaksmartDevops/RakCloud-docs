# linux系统yum报错没有足够的缓存安装

问题描述：使用yum安装时，报错提示没有足够的缓存来进行安装

![](./images/37403f3a63556f9f.png)

解决办法：更换yum源

## 备份原有yum源

mv /etc/yum.repos.d /etc/yum.repos.d.bak

## 创建yum源目录

mkdir /etc/yum.repos.d

## 下载yum源配置 （华为云源、阿里云源选择其一即可）

wget -O /etc/yum.repos.d/CentOS-Base.repo <https://repo.huaweicloud.com/repository/conf/CentOS-7-reg.repo>

wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo

## 重建缓存

yum clean all

yum makecache

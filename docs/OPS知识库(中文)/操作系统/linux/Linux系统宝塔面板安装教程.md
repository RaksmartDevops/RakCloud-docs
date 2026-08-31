# Linux系统宝塔面板安装教程

一、安装要求：

1.内存：512M以上，推荐768M以上（纯面板约占系统60M内存）

2.硬盘：300M以上可用硬盘空间（纯面板约占20M磁盘空间）

3.系统：CentOS 7.1+ (Ubuntu16.04+、Debian9.0+)，确保是干净的操作系统，没有安装过其它环境带的Apache/Nginx/php/MySQL/pgsql/gitlab/java（已有环境不可安装

4.架构：x86\_64

5.宝塔linux7.0版本是基于centos7开发的，务必使用centos7.x 系统 
提示：Centos官方已宣布在2020年停止对Centos6的维护更新，各大软件开发商也逐渐停止对Centos6的兼容，新服务器不建议使用Centos6

二、宝塔Linux面板7.9.0安装方法：

1. CentOS 8官方已经停止支持、请更换CentOS7系统或CentOS 8 Stream系统安装宝塔，详细说明：[Centos 8升级至Centos 8 Stream教程 - Linux面板 - 宝塔面板论坛 (bt.cn)](https://www.bt.cn/bbs/thread-82931-1-1.html)

1.CentOS安装命令：

Yum install -y wget && wget -O install.sh https://download.bt.cn/install/install\_6.0.sh && sh install.sh 12f2c1d72

2.Ubuntu/Deepin安装命令：

wget -O install.sh https://download.bt.cn/install/install-ubuntu\_6.0.sh && sudo bash install.sh 12f2c1d72

3.Debian安装命令：

wget -O install.sh https://download.bt.cn/install/install-ubuntu\_6.0.sh && bash install.sh 12f2c1d72

4.Fedora安装命令：

wget -O install.sh https://download.bt.cn/install/install\_6.0.sh && bash install.sh 12f2c1d72

5.Linux面板升级7.9.8命令：

curl https://download.bt.cn/install/update\_panel.sh|bash

三、以上节点如果无法使用，请使用下面的备用节点安装：

1.备用节点广东：

yum install –y wget && wget –O install.sh <http://125.88.182.172:5880/install/install> 6.0.sh && sh install.sh

2.备用节点香港：

yum install –y wget && wget –O install.sh <http://103.224.251.67:5880/install/install> 6.0sh && sh install.sh

3.备用节点美国：

Yum install –y wget && wget –O install.sh <http://128.1.164.196:5880/install/install> 6.0.sh && sh install.sh

使用SSH连接工具，如xshell、putty连接到您的Linux服务器后，根据系统执行相应的命令开始安装（大约2分钟完成面板安装），安装完成后会提示登录信息，如您需要更改密码、重启宝塔、修改端口、卸载宝塔等操作，可以直接输入：bt就会显示出对应的操作选项，如下图所示，根据提示完成操作即可。 

![](./images/720eaa1739931b35.png)

四、Linux面板7.9.8更新功能：

1.增加登录表单数据的RSA加密验证机制

2.增加敏感数据（用户名、密码等）的加密存储机制

3.优化关键数据传输加密机制及会话绑定机制，防止重放攻击

4.同步部分测试版已验证的Bug修复

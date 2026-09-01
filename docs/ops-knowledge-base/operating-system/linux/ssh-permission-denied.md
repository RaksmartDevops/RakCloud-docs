---
title: SSH登录Linux时提示“Permission denied, please try again”错误如何处理
---

问题：

通过本地SSH客户端登录Linux系统的ECS实例时，即便输入了正确的密码，出现了类似如下的错误信息。

- Permission denied, please try again
- SSH服务器拒绝了密码，请再试一次

原因：

1. ECS实例内禁用root用户登录：SSH服务对应配置文件`/etc/ssh/sshd_config`中的参数`PermitRootLogin`或`PasswordAuthentication`被设置为`no`。

可以参考下面的禁止root用户登录引起问题的解决方法

2.Linux系统启用了SELinux服务，导致root用户和普通用户无法登录。

执行`cat /var/log/secure`查看secure日志，若日志中包含`error: Could not get shadow infromation for root.`表示是启用了SELinux服务导致。

可以参考下面的SELinux服务引起问题的解决方法解决。

解决方法

一．禁止root用户登录引起问题的解决方法

1. 以VNC方式登录

2. 查看/etc/ssh/sshd\_config的参数PermitRootLogin或PasswordAuthentication配置。

- #cat /etc/ssh/sshd\_config

如下图所示，PermitRootLogin和PasswordAuthentication参数设置为no，表示禁止root用户登录，也禁止以密码方式登录。

![](./images/97cd4f92dcf51275.png)

3. 根据业务需要，修改PermitRootLogin和PasswordAuthentication参数配置

- 打开SSH配置文件
- vi /etc/ssh/sshd\_config

4. 修改PermitRootLogin和PasswordAuthentication参数值配置

- 如果需要root用户登录，请将PermitRootLogin参数值设置为yes
- 如果需要密码方式登录，请将PasswordAuthentication参数值设置为yes

![](./images/0f731e3c9d0ce28f.png)

5.按Esc键，输入:wq保存修改

6.执行如下命令，重启SSH服务

- systemctl restart sshd.service

二．SELinux服务引起问题的解决方法

可以根据实际情况，选择临时或永久关闭SELinux服务解决SSH连接异常问题。

检查SELinux服务状态

1. 以VNC方式登录ECS实例

2. 执行如下命令，查看当前SELinux服务状态

- /usr/sbin/sestatus -v

系统显示类似如下

SELinux status:       enabled

SELinux status参数值说明如下：

enabled：SELinux服务处于开启状态

disabled：SELinux服务处于关闭状态

3.关闭SELinux服务



临时关闭SELinux服务重启后会失效

执行如下命令，临时关闭SELinux

- setenforce 0

执行如下命令，永久关闭SELinux服务。

- sed -i 's/SELINUX=enforcing/SELINUX=disabled/' /etc/selinux/config

此命令只适用当前SELinux服务为enforcing状态时使用

4.重启实例使设置生效

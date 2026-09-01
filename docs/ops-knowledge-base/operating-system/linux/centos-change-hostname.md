---
title: CentOS系统修改主机名
---

方法一：

1.打开终端或通过ssh登录到Linux系统中

2.使用root权限登录系统

3.使用以下命令检查当前主机名：

- hostname

![](./images/05c55737d4acbca8.png)

4.使用以下命令修改主机名：

- hostnamectl set-hostname <new\_hostname>

其中，<new\_hostname>是您想要设置的新主机名

![](./images/0ce0202f729efa22.png)

5.重新启动Linux系统或者使用以下命令重启网络服务：

- systemctl restart systemd-hostnamed

![](./images/19864380684bdd7c.png)

6.使用以下命令验证主机名是否已经修改成功：

- hostname

![](./images/cd52a53a8f29da0b.png)

如果输出与新主机名相同，则表示修改主机名成功

将系统重启后，查看修改已生效

![](./images/136060aba4f0d6c3.png)

**方法二：**

1.打开/etc/hostname文件，使用以下命令：

- vi /etc/hostname

![](./images/8f73aff49596c2c0.png)

![](./images/0bd7b773a4e80b5a.png)

2.在打开的文件中修改主机名为您想要设置的您主机名

输入a即可进行编辑，将之前的主机名删除后设置您的新主机名，修改完成后，按Esc退出编辑模式，按Shift+：输入wq保存退出即可

![](./images/b254dce9f655e54d.png)

3.重新启动Linux系统后查看主机名已生效

![](./images/223ab64d49ce74ae.png)

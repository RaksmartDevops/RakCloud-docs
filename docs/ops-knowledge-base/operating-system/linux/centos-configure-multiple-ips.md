---
title: CentOS 操作系统如何配置多个IP
---

一.可以使用Linux\_tools.sh脚本自动添加

- 下载安装链接：[system tools](https://billing.raksmart.com/whmcs/index.php?rp=/knowledgebase/189/system-tools.html)

![](./images/36805aca49ed6468.png)

使用说明：

- 在任何等待输入界面，输入0可返回菜单，默认脚本退出会自动删除，有时候会失败，需要手动删除一下

配置IP功能：

- IP配置功能支持CentOS6-8系列和Ubuntu14-22系统及Debian系统

整段IP配置和连续IP配置必须严格按照提示的示例输入

- 如果系统只有一块网卡是UP状态，IP默认会配置在UP的网卡上；如果有多块网卡是UP状态，可以选择配置IP的网卡

- CentOS配置IP时，默认直接回车，IP会配置在网卡主配置文件中；如果选择以range形式配置时，生效较慢，存在执行重启网络服务命令超时的情况，实际配置已经在陆续生效中，请不要重复执行重启网络服务的命令

- Ubuntu系统重启网络服务时可能存在报错情况，如果检查配置文件没有问题（一般是配置文件中行对齐的问题），直接reboot重启后会生效

- 如有不明白，可输入9查看帮助

二、手动配置

1.首先需确认配置网卡名称

可以使用命令：ip a 查看网卡状态以及您机器其他的IP都有哪些，确认将您新添加的多个IP配置在哪个网卡中

- 查看网卡名称为eth0

- 查看您机器之前的IP配置在eth0网卡中

- 查看该网卡状态为UP，UP表示网卡是打开的也就是连接了外网

![](./images/aec5bf5016c43af0.png)

2.主网卡IP配置

执行：cd /etc/sysconfig/network-scripts/ 进入网卡配置文件目录

ls 查看目录下有哪些文件

![](./images/0064da179de1d490.png)

网卡名称为ifcfg-eth0，以下两种命令都可执行。

绝对路径执行命令：vi ifcfg-eth0 进入网卡配置文件中

相对路径执行命令：vi /etc/sysconfig/network-scripts/ifcfg-eth0 进入网卡配置文件中

比如需要配置一段/29的IP（可使用5个），数字12345代表的是IP的顺序，其中网关只需要书写一条即可，按照如下格式书写：

进入网卡配置文件后输入a，使用上下键进行移动到最后一行，添加要写入的配置即可，最后按ESC键，退出编辑模式

输入Shift+：，在输入wq保存退出按回车即可

- IPADDR=需要您将分配的IP写入

- NETMASK=分配IP的子网掩码

- GATEWAY=分配IP的网关

![](./images/430b8763338b8d11.png)

3.重启网卡使其配置生效

执行命令：systemctl restart network

4.附加网卡IP配置

还是在/etc/sysconfig/network-scripts/目录下，需要新创建子网卡配置文件，命名为range，如果您配置的是4CIP（4\*/26）或者8CIP（8\*/27），每一段IP都可以配置一个range子文件

起始为range0，range1，range2，range3 …………依次类推

下面还是以添加一段/29为例，以下两种命令都可执行

绝对路径执行命令：vi /etc/sysconfig/network-scripts/ifcfg-eth0-range0

相对路径执行命令：ifcfg-eth0-range0

![](./images/6373ec83859aa52e.png)

配置命令如下：

- IPADDR\_START= 起始IP
- IPADDR\_END= 末尾IP
- PREFIX=29 掩码
- CLONENUM\_START=0 子网起始数

进入网卡配置文件后输入a，，添加要写入的配置即可，最后按ESC键，退出编辑模式。输入Shift+：，在输入wq保存退出按回车即可。

![](./images/5a50422c0dcb2a46.png)

5.重启网卡使其配置生效。

执行命令：systemctl restart network

如果您以上两种方法都尝试配置均没有生效，请您及时发工单联系技术人员帮您处理。

---
title: Windows 服务器一键部署幻兽帕鲁
---

部署环境

- 服务器套餐配置：以CPU 4核、内存 16GB为例（通常可以满足6-8人同时在线联机）
- 操作系统：Windows Server 2019

登录 Windows 服务器

1、登录raksmart控制台，获取服务器登录密码。如您忘记密码，可以在控制台重置密码：

![](./images/image-cn2024.png)

2、使用电脑的“远程桌面连接”功能，输入IP地址、端口和账号，最后输入密码对服务器进行远程连接

![](./images/image-cn20241.png)

部署

前置知识：PowerShell

Windows的一键部署需要借助 PowerShell 来完成。PowerShell是一种任务自动化和配置管理框架，它提供了一个命令行Shell和脚本语言，用于管理和控制Windows操作系统和相关应用程序。那么要如何找到 PowerShell ？方法如下：

|  |  |
| --- | --- |
| 方法 | 描述 |
| 使用开始菜单 | 点击Windows开始按钮，然后在搜索框中输入"PowerShell"。你应该能够看到"Windows PowerShell"或"PowerShell"的搜索结果。点击该结果即可打开PowerShell。 |
| 使用运行对话框 | 按下Win + R键组合，打开运行对话框。在对话框中输入"powershell"，然后点击"确定"按钮即可打开PowerShell。 |
| 使用文件资源管理器 | 打开文件资源管理器（Windows资源管理器），导航到所需的目录，然后在地址栏中输入"powershell"并按下回车键。这将在当前目录中打开PowerShell。 |

第一步：下载 C++运行库（点击链接即可下载），需要手动安装。[https://aka.ms/vs/17/release/vc\_redist.x64.exe](https://cloud.tencent.com/developer/tools/blog-entry?target=https%3A%2F%2Faka.ms%2Fvs%2F17%2Frelease%2Fvc_redist.x64.exe&source=article&objectId=2383611 "https://cloud.tencent.com/developer/tools/blog-entry?target=https%3A%2F%2Faka.ms%2Fvs%2F17%2Frelease%2Fvc_redist.x64.exe&source=article&objectId=2383611")

第二步：下载 DirectX 支持库（点击链接即可下载），需要手动安装。[https://www.microsoft.com/en-us/download/details.aspx?id=35](https://cloud.tencent.com/developer/tools/blog-entry?target=https%3A%2F%2Fwww.microsoft.com%2Fen-us%2Fdownload%2Fdetails.aspx%3Fid%3D35&source=article&objectId=2383611 "https://cloud.tencent.com/developer/tools/blog-entry?target=https%3A%2F%2Fwww.microsoft.com%2Fen-us%2Fdownload%2Fdetails.aspx%3Fid%3D35&source=article&objectId=2383611")

第三步：运行一键部署命令

一键部署的方式适用于想要快速上手幻兽帕鲁服务器的开发者，仅需运行一行命令即可完成部署。

我们参考官方教程，为您封装好了一键部署幻兽帕鲁的脚本，并且上传到云端，您仅需要登录服务器，复制并在 PowerShell 中运行如下命令，通常等待3-5分钟后，即可完成幻兽帕鲁的部署。

iex (irm 'https://pal.pet/pal-server/Windows/install.ps1')

⚠️注意：如果您使用中国内地地域的服务器运行一键部署脚本，则有可能因为网络原因导致脚本运行失败，建议您多次重试或换个时间段再次部署。此处的原因主要是安装过程中需要请求Steam的服务器，网络连接状况可能不稳定。

第四步：关闭防火墙

![](./images/image-cn20242.png)

⚠️注意：一定要关闭机器内的防火墙，否则服务器可能会连接不上

服务端启动与重启

服务端部署完成后，会自动启动。无需额外再次启动

服务器重启后，幻兽帕鲁服务端会自动启动

如果需要重启服务端，直接重启服务器即可

登录游戏

前置条件

- 首先您需要在本地电脑中下载Steam客户端。
- 其次需要在Steam[购买幻兽帕鲁（Palworld）](https://cloud.tencent.com/developer/tools/blog-entry?target=https%3A%2F%2Fstore.steampowered.com%2Fapp%2F1623730%2FPalworld%2F%3Fl%3Dschinese&source=article&objectId=2382000 "https://cloud.tencent.com/developer/tools/blog-entry?target=https%3A%2F%2Fstore.steampowered.com%2Fapp%2F1623730%2FPalworld%2F%3Fl%3Dschinese&source=article&objectId=2382000")。

登录步骤

第一步：打开Steam客户端，并登录您的Steam账号。

![](./images/image-cn20243.png)

第二步：在“库”中找到幻兽帕鲁，并点击【开始游戏】。

![](./images/image-cn20244.png)

第三步：在游戏菜单选择【加入多人游戏（专用服务器）】。

![](./images/image-20245.png)

第四步：至此，您已经成功搭建了幻兽帕鲁专属服务器（Dedicated Server），可以让玩家输入您已部署服务器的公网IP地址和端口好（如11.11.11.11:8211），连接服务器成功后即可畅快联机开玩。

⚠️注意：切记在公网IP与端口中间使用英文冒号，否则会提示`Format Error. Example: 127.0.0.1:7777`！！！

![](./images/image-cn20246.png)

提示：您可以前往用户后台查看服务器的公网IP。在输入服务器的连接地址时，如您的服务器公网IP展示为：175.xxx.xx.138，则您需要在输入链接时填入：175.xxx.xx.138:8211

更新

打开PowerShell

输入一下命

iex (irm 'https://pal.pet/update\_windows.ps1')

稍等片刻，等待任务执行成功即可完成更新。

手动配置游戏参数

幻兽帕鲁部署完成之后，如果您想要按照自己的喜好来对游戏世界进行 DIY，那么还需要进行如下步骤：

第一步：前往如下路径找到游戏世界参数的配置文件：`PalWorldSettings.ini`

C:\Program Files\PalServer\steam\steamapps\common\PalServer\Pal\Saved\Config\WindowsServer\PalWorldSettings.ini

![](./images/image-cn20247.png)

第二步：选中该文件，右键单击，打开方式选择记事本。

第三步：按照您的需求写入具体的世界配置，以下内容仅作为示例，详细参数可查看[官方说明](https://cloud.tencent.com/developer/tools/blog-entry?target=https%3A%2F%2Ftech.palworldgame.com%2Foptimize-game-balance&source=article&objectId=2383611 "https://cloud.tencent.com/developer/tools/blog-entry?target=https%3A%2F%2Ftech.palworldgame.com%2Foptimize-game-balance&source=article&objectId=2383611")。

Difficulty=None ServerName=Lighthouse ServerDescription=Lighthouse AdminPassword=ABC ServerPassword=TEST DeathPenalty=All bEnablePlayerToPlayerDamage=False

第四步：重启服务器后即可生效（您部署的幻兽帕鲁将会随之自启动）

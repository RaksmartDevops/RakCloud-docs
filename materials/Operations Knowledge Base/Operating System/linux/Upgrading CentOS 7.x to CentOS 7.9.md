# Upgrading CentOS 7.x to CentOS 7.9

1.Open the terminal or SSH into the Linux system.

2.Log in to the system using root privileges.

3.To check the current system version, use the following command:

- cat /etc/ redhat-release

![](./images/5782b4c09f95279d.png)

4.To upgrade to CentOS 7.9 operating system, run the following commands:

- yum install update -y

"yum install <package\_name>": The command "<package\_name>" is used to install a specific software package. You need to replace "<package\_name>" with the actual name of the package you want to install. Adding the "-y" option allows for automatic confirmation of prompts during the installation process. "yum update" is used to update all installed software packages in the system to their latest versions.

![](./images/b396ecb60cf503d2.png)

The installation process may take some time. Please wait for the installation to complete. When you see the message "Complete!", it means that the installation is finished.

![](./images/834d7ebd9a0a3b5b.png)

5.You can use the command "cat /etc/redhat-release" to check if you have successfully upgraded to CentOS 7.9.

![](./images/38779ac96eccb809.png)

# CentOS 7.x Firewall: Enable/Disable and Add Ports

In CentOS 7.x, the default firewall is firewalld. Here is an example using CentOS 7.6

![](./images/8f5d498cae641a18.png)

1.To check the firewall status, run the command: `sudo firewall-cmd --state`

![](./images/a3ed271112d4ae19.png)

If the firewall status shows "not running," it means that the firewall is not enabled.

2.To enable the firewall, you can use the following command: `systemctl start firewalld`.

![](./images/e562e566e345a73e.png)

"Running" indicates that the firewall is currently active and running.

3.disable the firewall, you can run the command: `systemctl stop firewalld.service`.

![](./images/e06371307983740d.png)

3. 4.restart the firewall, you can run the command: `systemctl restart firewalld.service`.

5.To view all open ports in the firewall, you can use the command: `firewall-cmd --zone=public --list-ports `.

![](./images/dd63f46f7dfff985.png)

As shown in the above image, only port 13360 is open, which is the remote port number.

5. 6.Open port

firewall-cmd --zone=public --add-port=80/tcp --permanent # Open port 80

![](./images/6aec45dc38ba91a3.png)

The return value "success" indicates that the port has been successfully opened.

7.firewall-cmd --reload # Make the configuration take effect immediately.

![](./images/44f14741915f66c0.png)

As shown in the above figure, please check all the open ports of the firewall. Port 80 is currently open.

8.firewall-cmd --zone=public --remove-port=80/tcp --permanent  #Close port 80.

![](./images/f167f89578bdedd6.png)

9.After closing port 80, check that port 80 is closed once the configuration takes effect.

# To change the network interface name in CentOS 7.x

一.modify GRUB

1.Edit the GRUB configuration file by running the command: `vi /etc/default/grub`.

![](./images/ef3b2f8bed720026.png)

2.And add "net.ifnames=0 biosdevname=0"

![](./images/c04e6b88e18a3b72.png)

3.After making the modifications, save and exit by typing ":wq!" or use "ZZ" to exit.

4.Run the command "grub2-mkconfig -o /boot/grub2/grub.cfg" to regenerate the GRUB configuration and update the kernel parameters.

![](./images/3cc8aa3afacc7cbf.png)

二.Rename the current network interface configuration file.

1.First, use the command "ip a" to check the current network interface names. Make sure not to modify any names that are already in use.

![](./images/2d251c5d14d7631d.png) 

2.cd /etc/sysconfig/network-scripts/  #Enter the network interface configuration file directory.

![](./images/b5d0d40d4e5d46f5.png) 

mv ifcfg-eno1 ifcfg-eth0                  #Rename the interface in "eth" format.

sed -i 's/eno1/eth0/g' ifcfg-eth0      #Modify "eno1" to "eth0" inside the file, and adjust the command according to the specific name.

![](./images/76d762e8484f736c.png) 

三.Reboot the system to apply the above changes.
reboot

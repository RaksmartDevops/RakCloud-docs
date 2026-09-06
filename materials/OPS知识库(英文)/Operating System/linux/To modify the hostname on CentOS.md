# To modify the hostname on CentOS

**Method One:**

1.Open a terminal or SSH into the Linux system.

2.Log in to the system with root privileges.

3.Use the following command to check the current hostname:

- hostname

![](./images/05c55737d4acbca8.png)

4.Use the following command to change the hostname:

- hostnamectl set-hostname <new\_hostname>

Replace new-hostname with the desired hostname you want to set.

![](./images/0ce0202f729efa22.png)

5.Reboot the system for the changes to take effect, or you can run the following command to apply the new hostname without rebooting:

- systemctl restart systemd-hostnamed

![](./images/19864380684bdd7c.png)

6.To verify if the hostname has been successfully changed, use the following command:

- hostname

![](./images/cd52a53a8f29da0b.png)

If the output matches the new hostname you set, it indicates that the hostname has been successfully changed. After rebooting the system, verify that the modification has taken effect.

![](./images/136060aba4f0d6c3.png)

**Method 2:**

1.Open the "/etc/hostname" file using the following command:

- vi /etc/hostname

![](./images/8f73aff49596c2c0.png)

![](./images/0bd7b773a4e80b5a.png)

2.To change the hostname to your desired name in the opened file

To start editing, press "a" and delete the previous hostname. Set your new hostname. After making the changes, press "Esc" to exit edit mode. Then, press Shift+":" and type "wq" to save and exit.

![](./images/b254dce9f655e54d.png)

3.After restarting the Linux system, check whether the hostname has taken effect.

![](./images/223ab64d49ce74ae.png)

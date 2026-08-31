# To disable automatic system updates on Windows

1.Remotely access the Windows instance using Remote Desktop.

2. Click on the Start button located in the bottom-left corner and open the Control Panel. Then, click on "System and Security".

![](./images/de939d4fe65a4191.png)

3. Click on "Windows Update".

![](./images/74a9a7b52000209c.png)

4. Click on "Change settings" in the left column.

![](./images/f9a4544911ae7c86.png)

5. Once in the "Change settings" window, select the option "Never check for updates".

![](./images/c9fd5ec06f9c1bd3.png)

6. By doing this, we have successfully disabled the update checking for the Windows system. However, the Windows Update service is still set to start automatically at system startup. Therefore, we also need to open the "Server Manager" application.

![](./images/39d57f22e4ea4f79.png)

7. After opening the "Server Manager" window, click on "Tools" at the top and select "Services" from the drop-down menu.

![](./images/0a82f347b93df1f0.png)

8. Locate "Windows Update" in the list, right-click on it, and select "Properties". In the Properties window, set the "Startup type" to "Disabled", and then click "OK".

![](./images/74384593cb7eca6a.png)

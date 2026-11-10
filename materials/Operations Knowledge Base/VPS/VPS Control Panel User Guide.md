# VPS Control Panel User Guide

## Purpose

This document introduces the main functions and basic operations available in the VPS control panel, helping customers quickly become familiar with managing their VPS through the Raksmart Client Portal.

For features such as Upgrade/Downgrade, Elastic IP, Cloud Disk, Security Groups, and Snapshots, this document provides only a brief overview. For detailed instructions, please refer to the corresponding knowledge base articles.

**Supported Product:**

- VPS (Virtual Private Server)

---

# 1. Accessing the VPS Control Panel

### Steps

1. Log in to the **Raksmart Client Portal**.
2. Go to **Product Management → VPS**.
3. Select the VPS you want to manage.
4. Open the VPS details page.

The page displays basic server information, including:

- Region
- CPU
- Memory
- Operating System
- IP Address
- Login Password (copy supported)
- VNC
- Upgrade/Downgrade

---

# 2. Server Information

The left panel displays the basic information of your VPS, including:

- Region
- CPU
- Memory
- System Disk Specifications
- Username
- SSH Port (Linux)
- Notes (if configured)

Customers can quickly view the current server configuration and login information from this page.

---

# 3. Power Management

The left panel provides the most commonly used power management functions.

Available options include:

- Power On
- Shut Down
- Reboot
- Force Shut Down
- Force Reboot
- Reset Password
- Reinstall OS
- Rescue System

The functions are described below.

---

## Power On

Starts a VPS that is currently powered off.

Typical use cases:

- The VPS has been shut down.
- Restarting services after maintenance.

---

## Shut Down

Performs a graceful shutdown of the operating system.

It is recommended to use this option before maintenance or when stopping services.

---

## Reboot

Performs a normal reboot of the VPS.

Typical use cases:

- Applying system updates.
- Activating configuration changes.
- Restarting the system after troubleshooting.

---

## Force Shut Down

Immediately powers off the VPS.

**Note:**

A force shutdown does not allow the operating system to shut down gracefully and may result in data loss or file system corruption. It should only be used when a normal shutdown is not possible.

---

## Force Reboot

Immediately restarts the VPS.

**Note:**

This option should only be used when the server is unresponsive and a normal reboot cannot be performed.

---

## Reset Password

Resets the system login password.

Typical use cases:

- Forgotten login password.
- Changing the default password after deployment.

For detailed instructions, please refer to:

**[Bare Metal Cloud Password Change & Reset Guide](https://billing.raksmart.com/whmcs/index.php?rp=%2Fknowledgebase%2F530%2F%E8%A3%B8%E6%9C%BA%E4%BA%91%E5%AF%86%E7%A0%81%E4%BF%AE%E6%94%B9%E4%B8%8E%E9%87%8D%E7%BD%AE%E6%8C%87%E5%8D%97.html&language=english)**

---

## Reinstall OS

Reinstalls the operating system of the VPS.

Linux and Windows operating systems are supported, depending on the available options shown in the control panel.

**Note:**

Reinstalling the operating system will erase all data on the system disk. Please back up important data before proceeding.

For detailed instructions, please refer to:

**[Bare Metal Cloud OS Reinstallation Guide](https://billing.raksmart.com/whmcs/index.php?rp=%2Fknowledgebase%2F1155%2F%E8%A3%B8%E6%9C%BA%E4%BA%91%E9%87%8D%E8%A3%85%E7%B3%BB%E7%BB%9F%E6%8C%87%E5%8D%97.html&language=english)**

---

## Rescue System

When the operating system cannot boot normally, you can enter Rescue Mode to repair the system or recover data.

Typical use cases:

- Operating system fails to boot.
- File system repair.
- Boot configuration recovery.
- Data recovery.

For detailed instructions, please refer to:

**[Bare Metal Cloud Rescue System Guide](https://billing.raksmart.com/whmcs/index.php?rp=%2Fknowledgebase%2F525%2F%E8%A3%B8%E6%9C%BA%E4%BA%91-Rescue%E6%95%91%E6%8F%B4%E7%B3%BB%E7%BB%9F%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97.html&language=english)**

---

# 4. VNC Console

Click the **VNC** button at the top of the page to open the server console.

The VNC console allows you to access the server even if network connectivity is unavailable.

Typical use cases:

- SSH connection failure.
- Remote Desktop (RDP) connection failure.
- Password recovery.
- Viewing the boot process.
- System maintenance.

For detailed instructions, please refer to:

**[Bare Metal Cloud VNC Console Guide](https://billing.raksmart.com/whmcs/index.php?rp=%2Fknowledgebase%2F1153%2F%E8%A3%B8%E6%9C%BA%E4%BA%91-VNC-%E6%8E%A7%E5%88%B6%E5%8F%B0%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97.html&language=english)**

---

# 5. Upgrade/Downgrade

Click the **Upgrade/Downgrade** button at the top of the page to adjust your VPS resources according to your business requirements.

Available upgrade or downgrade options may include:

- CPU
- Memory
- Bandwidth
- Traffic

The available resources depend on the options displayed in the control panel.

For detailed instructions, please refer to:

**[Bare Metal Cloud Upgrade/Downgrade Guide](https://billing.raksmart.com/whmcs/index.php?rp=%2Fknowledgebase%2F1139%2F%E8%A3%B8%E6%9C%BA%E4%BA%91%E5%8D%87%E7%BA%A7or%E9%99%8D%E7%BA%A7%E6%93%8D%E4%BD%9C%E6%8C%87%E5%8D%97.html&language=english)**

---

# 6. Charts

The **Charts** page displays real-time monitoring information for your VPS.

Available monitoring metrics include:

- CPU Usage
- Disk I/O
- Memory Usage
- Network Traffic

These charts help you monitor the operating status and resource utilization of your VPS.

For more information, please refer to:

[**VPS Monitoring Features Guide**](https://billing.raksmart.com/whmcs/index.php?rp=%2Fknowledgebase%2F810%2FVPS-%E7%9B%91%E6%8E%A7%E5%8A%9F%E8%83%BD%E8%AF%B4%E6%98%8E.html&language=english)

---

# 7. Usage

The **Usage** page displays network traffic statistics for your VPS.

You can:

- View historical traffic usage.
- Select a custom date range.
- Review traffic statistics for a specific period.

This information can help analyze bandwidth consumption and network usage trends.

---

# 8. Elastic IP

The **Elastic IP** page allows you to manage Elastic IP addresses purchased for your VPS.

Supported operations include:

- Viewing Elastic IPs.
- Binding an Elastic IP.
- Unbinding an Elastic IP.

For detailed instructions, please refer to:

[**VPS Elastic IP Guide**](https://billing.raksmart.com/whmcs/index.php?rp=%2Fknowledgebase%2F918%2FVPS-%E5%BC%B9%E6%80%A7-IP-%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97.html&language=english)

---

# 9. Cloud Disk

The **Cloud Disk** page allows you to manage purchased Cloud Disks.

Supported operations include:

- Viewing Cloud Disks.
- Attaching a Cloud Disk.
- Detaching a Cloud Disk.

**Note:**

After attaching a Cloud Disk through the control panel, you must log in to the operating system to initialize, partition (if required), format (for first use), and mount the disk before it can be used.

For detailed instructions, please refer to:

[**VPS Cloud Disk Guide**](https://billing.raksmart.com/whmcs/index.php?rp=%2Fknowledgebase%2F915%2FVPS-%E7%8B%AC%E7%AB%8B%E4%BA%91%E7%9B%98%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97.html&language=english)

---

# 10. Security Groups

The **Security Groups** page allows you to manage network access policies for your VPS.

Supported operations include:

- Creating Security Groups.
- Managing Security Group rules.
- Attaching Security Groups.
- Detaching Security Groups.

Security Groups help control network access by allowing or denying specific ports and traffic.

For detailed instructions, please refer to:

[**VPS Security Group Guide**](https://billing.raksmart.com/whmcs/index.php?rp=/knowledgebase/1021/VPS-%E5%AE%89%E5%85%A8%E7%BB%84%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97.html)

---

# 11. Snapshots

The **Snapshots** page allows you to save the current state of your VPS for future recovery.

It is recommended to create a snapshot before:

- Performing system upgrades.
- Installing software.
- Modifying important configurations.
- Deploying production services.

**Note:**

Snapshots are intended for quick system recovery and should not replace regular data backups.

For detailed instructions, please refer to:

**VPS Snapshot Guide**

---

# 12. Frequently Asked Questions

### Q1: Why doesn't the VPS shut down immediately after clicking **Shut Down**?

The system performs a graceful shutdown. The time required depends on the operating system and the services currently running. Please wait a few moments and refresh the server status.

---

### Q2: When should I use **Force Shut Down** or **Force Reboot**?

These options should only be used when the VPS is unresponsive and cannot be shut down or restarted normally.

Whenever possible, use the standard **Shut Down** or **Reboot** options.

---

### Q3: Will reinstalling the operating system delete my data?

Yes.

Reinstalling the operating system erases all data stored on the system disk. Please back up important data before proceeding.

---

### Q4: What is the difference between VNC and SSH (or Windows RDP)?

SSH and RDP are network-based remote access methods, while VNC provides direct console access to the server.

Even if the network is unavailable or SSH/RDP cannot connect, you can usually still manage the server through the VNC console.

---

### Q5: Why are there no monitoring or usage statistics displayed?

If the VPS has just been created, powered on, or restored, monitoring data may require some time to be collected.

Please wait a few minutes and refresh the page.

---

# Notes

⚠️ Before performing operations such as reinstalling the operating system or upgrading resources, it is recommended to back up important data.

⚠️ Force Shut Down and Force Reboot should only be used when normal shutdown or reboot operations are not possible.

⚠️ After attaching a Cloud Disk, you must complete the disk initialization and mounting process within the operating system before it can be used.

⚠️ Snapshots are intended for quick recovery and should not be considered a replacement for regular backups. Regular backups of important business data are strongly recommended.

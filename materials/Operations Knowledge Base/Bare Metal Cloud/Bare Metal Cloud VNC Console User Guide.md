# Bare Metal Cloud VNC Console User Guide

## Purpose

This document describes how to access and use the VNC (Virtual Network Computing) console through the Bare Metal Cloud Control Panel, including common use cases and available features.

**Applicable Product:** Bare Metal Cloud

---

# 1. What is the VNC Console?

VNC (Virtual Network Computing) provides direct console access to your server.

Unlike SSH or Remote Desktop (RDP), VNC does not rely on the server's network services. Even if SSH or RDP is unavailable, you can usually still access and manage your server through the VNC console.

---

# 2. When Should You Use VNC?

It is recommended to use VNC in the following situations:

- SSH connection is unavailable (Linux)
- Remote Desktop (RDP) connection is unavailable (Windows)
- You have forgotten your server login password
- You need to modify network configurations
- You want to view the server boot process
- The operating system fails to start normally
- System maintenance or troubleshooting is required

---

# 3. How to Open the VNC Console

## Steps

1. Log in to the Raksmart Client Portal.
2. Navigate to **Product Management** → **Bare Metal Cloud**.
3. Select the server you want to manage.
4. Open the **Management** page.
5. Click **VNC**.
6. A new browser window will open automatically, and the VNC console connection will be established.
7. Once connected, the server console will be displayed.
8. Log in using your server's operating system username and password.

**Note:**

The VNC console uses your server's operating system credentials (for example, **root** for Linux or **Administrator** for Windows), not your Raksmart Client Portal account.

---

# 4. VNC Console Features

The following functions are available in the upper-right corner of the VNC console.

## Paste Password

Quickly paste a copied password into the server login screen.

Recommended when:

- The password is long or contains special characters.
- You want to avoid typing errors.

---

## Clipboard

The Clipboard feature allows you to copy and paste text between your local computer and the VNC console.

Common uses include:

- Copying commands to the server.
- Copying text from the server.
- Improving operational efficiency.

**Note:**

The Clipboard feature supports text only and does not support file transfer.

---

## Send Ctrl + Alt + Del

Sends the **Ctrl + Alt + Del** key combination to the server.

Common uses include:

- Accessing the Windows login screen.
- Opening Windows Security options.
- Unlocking a Windows session.
- Logging in to Windows systems that require **Ctrl + Alt + Del**.

---

# 5. What Can You Do with the VNC Console?

The VNC console allows you to perform most routine server management tasks, including:

- Log in to the server
- Change the system password
- Monitor the server boot process
- Modify network configurations
- Restart the server
- Diagnose system issues
- Perform system maintenance and troubleshooting

For Linux servers, you can also:

- Enter Single User Mode
- Repair system configurations
- View boot logs

---

# 6. Frequently Asked Questions

### Q1: Which username and password should I use to log in through VNC?

Use your server's operating system credentials.

For example:

- Linux: **root**
- Windows: **Administrator**

---

### Q2: Why can I access the server through VNC but not through SSH or RDP?

SSH and RDP depend on the server's network configuration and related services.

VNC connects directly to the server console, so it usually remains available even if the network configuration is incorrect or the remote access services are not running.

---

### Q3: Can I change my server password through VNC?

Yes.

After logging in to the operating system through VNC, you can change your password using the standard operating system method.

If you have forgotten your password, you can also use the **Reset Password** feature in the control panel.

For more information, please refer to the [**Bare Metal Cloud Password Change and Reset Guide**.](https://billing.raksmart.com/whmcs/index.php?rp=%2Fknowledgebase%2F530%2F%E8%A3%B8%E6%9C%BA%E4%BA%91%E5%AF%86%E7%A0%81%E4%BF%AE%E6%94%B9%E4%B8%8E%E9%87%8D%E7%BD%AE%E6%8C%87%E5%8D%97.html&language=english)

---

### Q4: Can I transfer files through the VNC console?

No.

The **Clipboard** feature supports text copy and paste only. It does not support file transfers.

To transfer files, we recommend using:

- **Linux:** SCP or SFTP
- **Windows:** Remote Desktop file sharing, FTP, or other file transfer tools

---

### Q5: Will closing the VNC browser window affect my server?

No.

Closing the VNC window only disconnects the current console session. It does not affect the operation of your server.

---

# Notes

⚠️ The VNC console uses your server's operating system credentials, not your Raksmart Client Portal account.

⚠️ VNC is recommended as an emergency access method when SSH or RDP is unavailable. For routine server management, SSH (Linux) or Remote Desktop (Windows) is still recommended.

⚠️ The Clipboard feature supports text only and does not support file transfers.

⚠️ Before making major system changes, it is recommended to back up your important data.

---

# Bare Metal Cloud OS Reinstallation Guide

## Purpose

This document describes how to reinstall the operating system through the Bare Metal Cloud Control Panel, including operating system selection, login method configuration, data retention rules, and important considerations to help you complete the reinstallation successfully.

**Applicable Product:** Bare Metal Cloud

---

# 1. Before Reinstalling the Operating System

Before proceeding with OS reinstallation, please note the following:

- Reinstalling the operating system will reinstall the OS and **format the system disk**.
- If your server has an additional **data disk**, **only the system disk will be formatted**. The data disk will **not** be formatted, and the data on it will be preserved.
- **After the reinstallation is complete, the data disk will not be mounted automatically. You will need to mount it manually before accessing the data.**
- Reinstalling the operating system will cause **all existing snapshots of the instance to become invalid and be automatically deleted**. Deleted snapshots cannot be recovered.
- If a **Custom Script** was configured when the instance was created, it will be executed automatically during the OS reinstallation. Modifying or re-entering the script is not supported.
- To prevent data loss, it is strongly recommended to back up all important data before proceeding.

---

# 2. How to Reinstall the Operating System

1. Log in to the **Raksmart Client Portal**.
2. Navigate to **Product Management** → **Bare Metal Cloud**.
3. Select the server you want to manage.
4. Open the **Management** page.
5. Click **Reinstall OS**.

A configuration window will appear.

---

# 3. Configure the Reinstallation Settings

## 1. Select the Operating System

Choose the operating system you want to install.

The available operating systems are determined by the options displayed in the control panel, such as:

- CentOS
- Ubuntu
- Debian
- Windows Server

---

## 2. Select the Login Method

Two login methods are available.

### Password Login

When selecting **Password Login**, you can configure the server login password.

You may choose to:

- Use a randomly generated password provided by the system.
- Set your own custom password.

---

### SSH Key Login

Linux operating systems support SSH Key authentication.

When selecting **SSH Key Login**, choose an SSH public key from the list of keys already added to your account.

If you have not created an SSH public key yet, please add one first.

> **For more information, please refer to the [*SSH Public Key Management Guide*](https://billing.raksmart.com/whmcs/index.php?rp=/knowledgebase/989/SSH-KEY-%E7%AE%A1%E7%90%86.html).**

---

## 3. Configure the SSH Port

For Linux systems, you may configure the SSH port.

You can choose to:

- Use a randomly generated port.
- Specify a custom SSH port.

> **Recommendation:**
>
> If you change the default SSH port, make sure the corresponding port is allowed in both the security group and the operating system firewall. Otherwise, SSH connections may fail.

---

# 4. Start the OS Reinstallation

After confirming that all settings are correct, click **Confirm** to start the reinstallation.

The system will automatically perform the following operations:

- Format the system disk.
- Install the selected operating system.
- Configure the login method.
- Configure the login password or SSH public key.
- Configure the SSH port (Linux only).

Once the installation is complete, you can log in using the newly configured credentials.

---

# 5. Disk and Data Information

## System Disk

During the OS reinstallation, the system disk will be formatted and a fresh operating system will be installed.

All data stored on the system disk will be erased.

---

## Data Disk

If the server has an additional data disk:

- The data disk will **not** be formatted during OS reinstallation.
- Existing data on the data disk will be preserved.
- The data disk will **not** be mounted automatically after the reinstallation.

After logging into the server, manually mount the data disk before accessing the stored data.

---

## Disk Partition Information

Disk partitions cannot be modified during the OS reinstallation process.

For servers with both a system disk and a data disk:

- The existing disk layout will remain unchanged.
- The system disk and data disk cannot be merged.
- If you need to redesign the disk layout, back up your data first and redeploy the server as needed.

---

# 6. Additional Information

## Custom Script

If a **Custom Script** was configured when the instance was created:

- The same Custom Script will be executed automatically during the OS reinstallation.
- Modifying or re-entering the Custom Script is not supported.

---

## Snapshots

After reinstalling the operating system:

- All existing snapshots of the instance will become invalid.
- All snapshots will be deleted automatically.
- Deleted snapshots cannot be recovered.

If your snapshots contain important data, please back up the data before reinstalling the operating system.

---

# 7. Recommended Checks After Reinstallation

After the operating system has been installed, verify the following:

✅ You can successfully log in using the new login credentials.

✅ The correct operating system has been installed.

✅ SSH access is working properly (Linux).

✅ Remote Desktop (RDP) access is working properly (Windows).

✅ If the server has a data disk, it has been mounted successfully.

✅ Applications and services are functioning as expected.

---

# 8. Frequently Asked Questions

### Q1: What data will be deleted during OS reinstallation?

Only the **system disk** will be formatted.

If the server has an additional data disk, the data disk will not be formatted, and its data will remain intact.

---

### Q2: Why can't I see my data disk after the reinstallation?

Your data disk has not been deleted.

After reinstalling the operating system, the data disk is **not mounted automatically**. You must manually mount the data disk before accessing its contents.

---

### Q3: Can I set my own login password?

Yes.

When using **Password Login**, you may either use the system-generated password or specify your own custom password.

---

### Q4: When should I use SSH Key authentication?

SSH Key authentication is recommended for Linux servers.

Compared with password authentication, SSH Keys provide stronger security and help protect against password leaks and brute-force attacks.

If you plan to use SSH Key authentication, please add an SSH public key to your account first.

---

### Q5: Will the Custom Script be executed again after reinstalling the operating system?

Yes.

The Custom Script configured when the instance was created will be executed automatically during the reinstallation process. It cannot be modified or replaced.

---

### Q6: Can snapshots be restored after reinstalling the operating system?

No.

All existing snapshots will be automatically deleted during the OS reinstallation process and cannot be recovered.

---

### Q7: Can I modify the disk partitions during OS reinstallation?

No.

Disk partitions cannot be modified during the reinstallation process. The existing system disk and data disk layout will remain unchanged and cannot be merged.

---

# Notes

⚠️ Back up all important data before reinstalling the operating system.

⚠️ Only the system disk is formatted during OS reinstallation. The data disk is preserved but must be mounted manually after the installation is complete.

⚠️ All existing snapshots of the instance will be automatically deleted during OS reinstallation and cannot be recovered.

⚠️ Disk partitions cannot be modified during the reinstallation process. The existing system disk and data disk layout will remain unchanged.

⚠️ If you change the SSH port, make sure the corresponding port is allowed by both the security group and the operating system firewall.

⚠️ The Custom Script configured when the instance was created will be executed automatically during the reinstallation process and cannot be modified.

---

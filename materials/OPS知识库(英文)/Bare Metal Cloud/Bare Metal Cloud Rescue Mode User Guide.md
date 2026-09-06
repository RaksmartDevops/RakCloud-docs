# Bare Metal Cloud Rescue Mode User Guide

## Purpose

This document explains how to use the Rescue Mode feature through the Bare Metal Cloud Control Panel, including its applicable scenarios, configuration options, login methods, and important considerations. It is designed to help you perform system maintenance, troubleshooting, and data recovery when your server encounters issues.

**Applicable Product:** Bare Metal Cloud

---

# 1. What is Rescue Mode?

Rescue Mode is a temporary maintenance environment that runs independently from your server's installed operating system.

When the operating system fails to boot, or you cannot access the server via SSH or Remote Desktop (RDP), Rescue Mode allows you to start the server in a separate environment for system maintenance, troubleshooting, and data recovery.

> **Note:**
>
> Rescue Mode does **not** reinstall the operating system or format your disks. It provides a temporary maintenance environment for troubleshooting and recovery purposes.

---

# 2. When Should I Use Rescue Mode?

Rescue Mode is recommended in the following situations:

- The operating system fails to boot.
- Unable to connect via SSH (Linux).
- Unable to connect via Remote Desktop (RDP) (Windows).
- Incorrect system configuration prevents login.
- System files or configuration need to be repaired.
- Important data needs to be backed up or recovered.
- Disk inspection or other system maintenance is required.

---

# 3. Entering Rescue Mode

1. Log in to the **Raksmart Client Portal**.
2. Navigate to **Product Management** → **Bare Metal Cloud**.
3. Select the server you want to manage.
4. Open the **Management** page.
5. Click **Rescue**.

A Rescue configuration window will appear.

---

# 4. Configure Rescue Mode

## 1. Select the Rescue System

Choose the appropriate Rescue system based on your maintenance requirements.

The following Rescue systems are currently available:

- Windows (Chinese)
- Windows (English)
- Linux

Please select the Rescue system that best fits your maintenance needs.

---

## 2. Set a Temporary Password

Before entering Rescue Mode, you must configure a temporary login password.

You may choose to:

- Use a system-generated random password.
- Set your own custom password.

> **Important:**
>
> **Please save the temporary password carefully. It will only be displayed once and cannot be viewed again.**
>
> It is recommended to copy or record the password before confirming the operation.

---

## 3. Confirm Force Shutdown

Before entering Rescue Mode, you must check the following option:

☑ **I agree to perform a forced shutdown**

> **Note:**
>
> Rescue Mode requires the server to reboot into a separate maintenance environment.
>
> A forced shutdown will be performed. Please ensure that service interruption is acceptable before proceeding.

---

# 5. Starting Rescue Mode

After confirming all settings, click **Confirm** to start Rescue Mode.

The system will automatically:

- Force shutdown the current server.
- Boot into the selected Rescue environment.
- Create a temporary login environment.

Once Rescue Mode has started successfully, you can log in using the temporary password you configured.

---

# 6. Logging in to Rescue Mode

Rescue Mode supports network connectivity, allowing you to log in remotely or through the VNC console.

## Linux Rescue

Supported login methods:

- SSH
- VNC Console

Default SSH port:

**22**

Use the username provided by the Rescue system and the temporary password configured when creating Rescue Mode.

---

## Windows Rescue

Supported login methods:

- Remote Desktop (RDP)
- VNC Console

Default Remote Desktop (RDP) port:

**3389**

Use the temporary password configured when creating Rescue Mode to log in.

---

# 7. What Can You Do in Rescue Mode?

After entering Rescue Mode, you can perform the following maintenance tasks:

- Check system configuration.
- Repair system files.
- Check disk status.
- Mount the system disk.
- Mount additional data disks.
- Back up or recover important data.
- Modify system configuration files.
- Troubleshoot system startup issues.
- Perform other maintenance and recovery operations.

> **Note:**
>
> If your server has one or more additional data disks, they **will not be mounted automatically** in Rescue Mode. You must mount them manually before accessing the data.

---

# 8. Exiting Rescue Mode

> After completing your maintenance tasks, you can exit Rescue Mode through the control panel.
>
> ### Steps
>
> 1. The **Rescue** button will now change to **Exit Rescue**.
> 2. Click **Exit Rescue**.
>
> The system will automatically:
>
> - Exit Rescue Mode.
> - Reboot the server.
> - Boot back into the original operating system.
>
> > **Note:**
> >
> > After clicking **Exit Rescue**, the server will reboot automatically. No additional manual restart is required.

---

# 9. Frequently Asked Questions

### Q1: Will entering Rescue Mode delete my server data?

No.

Rescue Mode does not reinstall the operating system, format disks, or delete any server data.

---

### Q2: Why is a forced shutdown required?

Rescue Mode runs in an independent maintenance environment.

The server must reboot into this environment, so a forced shutdown is required.

---

### Q3: Can I view the temporary password again later?

No.

The temporary password is displayed only once when Rescue Mode is created.

Please copy or record it before proceeding. If the password is lost, you will need to recreate Rescue Mode and set a new temporary password.

---

### Q4: What login methods are supported in Rescue Mode?

The following login methods are supported:

**Linux Rescue**

- SSH (Default Port: **22**)
- VNC Console

**Windows Rescue**

- Remote Desktop (RDP) (Default Port: **3389**)
- VNC Console

Please use the temporary password configured when creating Rescue Mode.

---

### Q5: Why can't I see my data disk after entering Rescue Mode?

Additional data disks are **not mounted automatically**.

Please manually mount the data disk after logging into Rescue Mode before accessing your data.

---

### Q6: How do I return to my original operating system?

After completing your maintenance tasks, click **Exit Rescue** in the control panel.

The system will automatically exit Rescue Mode, reboot the server, and boot back into the original operating system.

No additional manual reboot is required.

Q7: Does Rescue Mode support network connectivity?

Yes.

Rescue Mode supports network access by default.

You can connect remotely using:

- SSH (Linux)
- Remote Desktop (RDP) (Windows)
- VNC Console

---

# Notes

⚠️ Before entering Rescue Mode, ensure that service interruption is acceptable, as the server will be forcibly shut down.

⚠️ The temporary password is displayed only once. Please save it before proceeding.

⚠️ Rescue Mode does not reinstall the operating system or delete any server data.

⚠️ Rescue Mode supports network connectivity and can be accessed via SSH, Remote Desktop (RDP), or the VNC Console.

⚠️ The default SSH port for Linux Rescue is **22**, and the default Remote Desktop (RDP) port for Windows Rescue is **3389**.

⚠️ Additional data disks are not mounted automatically in Rescue Mode and must be mounted manually.

⚠️ After completing maintenance, be sure to exit Rescue Mode before restarting the server.

---

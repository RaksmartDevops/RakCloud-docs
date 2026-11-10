---
title: Bare Metal Cloud Control Panel User Guide
---

## Purpose

This document introduces the main functional modules and basic operations available in the Bare Metal Cloud Control Panel, helping users quickly become familiar with the management interface.

For features such as **Upgrade/Downgrade**, **Snapshots**, and **Security Groups**, this guide provides only a brief overview. Please refer to the corresponding knowledge base articles for detailed instructions.

**Applicable Product:** Bare Metal Cloud

---

## 1. Accessing the Bare Metal Cloud Control Panel

1. Log in to the **Raksmart Client Portal**.
2. Navigate to **Product Management** → **Bare Metal Cloud**.
3. Locate the Bare Metal Cloud server you want to manage.
4. Click the product name to enter the server management page.

The following functional modules are available at the top of the page:

- Management
- Configuration
- Monitoring
- Additional Features
- Applications
- Snapshots

---

## 2. Management

The **Management** page provides the most commonly used server management functions, including power control, system maintenance, and remote management.

## Refresh Status

Click **Refresh Status** to update the current operating status of the server.

Typical use cases:

- Check whether the server is powered on
- Verify whether a shutdown or reboot operation has completed

---

## Power On

When the server is powered off, click **Power On** to start the server.

Typical use cases:

- Restart a powered-off server
- Resume services after maintenance

---

## Shut Down

Click **Shut Down** to perform a normal operating system shutdown.

Recommended before:

- Hardware maintenance
- System configuration changes
- Long-term server downtime

> **Note:**
>
> Stop running services or ensure that no critical tasks are in progress before shutting down the server to avoid service interruption.

---

## Reboot

Click **Reboot** to restart the server normally.

Typical use cases:

- Apply system configuration changes
- Complete system updates
- Recover from system issues

---

## Force Power Off

Click **Force Power Off** to immediately turn off the server.

> **Warning:**
>
> A force shutdown does not allow the operating system to shut down properly and may result in data loss or file system corruption.
>
> Use this option only if the server cannot be shut down normally.

---

## VNC Console

The VNC Console provides direct access to the server console.

Even if the network connection is unavailable or SSH/RDP cannot be accessed, you can still manage the server through VNC.

Common use cases include:

- SSH connection failure
- Remote Desktop (RDP) connection failure
- System boot issues
- Changing the system password
- Entering single-user mode
- Viewing the system boot process

For detailed instructions, please refer to [**Bare Metal Cloud VNC Console User Guide**.](/operations-knowledge-base/baremetal/bare-metal-cloud-vnc-console-user-guide)

---

## Reset Password

Use this feature to reset the server's login password.

Typical use cases:

- Forgotten login password
- Initial password replacement

For detailed instructions, please refer to [**Bare Metal Cloud Password Change and Reset Guide**.](/operations-knowledge-base/baremetal/bare-metal-cloud-password-change-and-reset-guide)

---

## Reinstall Operating System

Use this feature to reinstall the operating system.

Supported operating systems include Linux and Windows (depending on the options available in the control panel).

> **Warning:**
>
> Reinstalling the operating system will erase all data on the system disk.
>
> Please back up any important data before proceeding.

For detailed instructions, please refer to [**Bare Metal Cloud OS Reinstallation Guide**](/operations-knowledge-base/baremetal/bare-metal-cloud-os-reinstallation-guide).

---

## Rescue Mode

If the operating system cannot boot normally, you can enter Rescue Mode to repair the system or recover data.

Common use cases include:

- Operating system boot failure
- File system repair
- Boot configuration repair
- Data recovery

For detailed instructions, please refer to [**Bare Metal Cloud Rescue Mode User Guide**](/operations-knowledge-base/baremetal/bare-metal-cloud-rescue-mode-user-guide).

---

## Upgrade / Downgrade

You can adjust your server resources according to your business requirements.

Available upgrade or downgrade options depend on your server configuration and may include:

- CPU
- Memory
- Bandwidth
- Traffic

For detailed instructions, please refer to [**Bare Metal Cloud Upgrade/Downgrade Guide**](/operations-knowledge-base/baremetal/bare-metal-cloud-upgrade-downgrade-guide).

---

## 3. Configuration

The **Configuration** page displays the current server specifications.

You can view information such as:

- CPU Configuration
- Memory Capacity
- System Disk
- Bandwidth Type
- Bandwidth Size
- Traffic Plan
- DDoS Protection IP (if purchased)

Use this page to verify your server specifications and network configuration.

> **Note:**
>
> This page is for viewing configuration information only. Server specifications cannot be modified directly from this page.

---

## 4. Monitoring

The **Monitoring** page allows you to view the server's resource usage and monitor its operating status.

The following monitoring metrics are currently available:

- CPU Usage
- Disk I/O
- Memory Usage
- Network Traffic
- Traffic Statistics

The monitoring charts help you analyze resource utilization, such as:

- Whether CPU usage remains consistently high
- Whether abnormal disk activity exists
- Whether memory resources are insufficient
- Whether network traffic is abnormal

For detailed instructions, please refer to [**Bare Metal Cloud Monitoring Guide**](/operations-knowledge-base/baremetal/bare-metal-cloud-monitoring-feature-guide).

---

## 5. Additional Features

The **Additional Features** page is primarily used for managing server network security.

The following functions are available:

- Create Security Groups
- Manage Security Groups
- Delete Security Groups
- Apply Security Groups to the server
- Remove Security Groups from the server

Security Groups allow you to control inbound network access and manage firewall rules, improving server security.

For detailed instructions, please refer to [**Bare Metal Cloud Security Group Guide**](/operations-knowledge-base/vps/vps-security-group-user-guide).

---

## 6. Applications

The **Applications** page is used to manage available system applications or additional features.

Available applications may vary depending on the product and operating system.

If no applications are displayed, no further action is required.

---

## 7. Snapshots

Snapshots allow you to save the current state of your server for future recovery.

It is recommended to create a snapshot before:

- Upgrading the operating system
- Installing software
- Modifying important system configurations
- Deploying production services

> **Note:**
>
> Snapshots are intended for quick system recovery and should not replace regular data backups.
>
> Important business data should still be backed up independently on a regular basis.

For detailed instructions, please refer to **Bare Metal Cloud Snapshot Guide**.

---

## 8. Frequently Asked Questions

### Q1: Why doesn't the server shut down immediately after I click **Shut Down**?

The server performs a normal operating system shutdown.

The required time depends on the operating system and currently running services.

Please wait a few moments and refresh the server status.

---

### Q2: When should I use **Force Power Off**?

Force Power Off should be used only when the server becomes unresponsive and cannot perform a normal shutdown.

Under normal circumstances, always use **Shut Down** first.

---

### Q3: Will reinstalling the operating system delete my data?

Yes.

Reinstalling the operating system erases all data on the system disk.

Please back up important data before reinstalling the operating system.

---

### Q4: What is the difference between VNC and SSH (or Windows Remote Desktop)?

SSH and Remote Desktop (RDP) are network-based remote access methods.

The VNC Console provides direct console access to the server.

Even if network connectivity is unavailable or SSH/RDP cannot be accessed, you can usually still manage the server through the VNC Console.

---

### Q5: Why can't I modify CPU, memory, or bandwidth from the Configuration page?

The **Configuration** page is for viewing your current server specifications only.

To change server resources, please use the **Upgrade/Downgrade** feature.

For detailed instructions, please refer to **Bare Metal Cloud Upgrade/Downgrade Guide**.

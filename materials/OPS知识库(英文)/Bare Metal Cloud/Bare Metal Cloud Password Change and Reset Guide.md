# Bare Metal Cloud Password Change and Reset Guide

# Purpose

This document describes how to change and reset passwords for Bare Metal Cloud servers. It applies to both Linux and Windows operating systems and helps users quickly complete password-related operations when they need to change or reset their server password.

**Applicable Product:** Bare Metal Cloud

---

# 1. Difference Between Changing and Resetting a Password

Before proceeding, please confirm which operation you need.

|  |  |
| --- | --- |
| Operation | Applicable Scenario |
| **Change Password** | You can log in to the server normally and want to change your current login password. |
| **Reset Password** | You have forgotten the server password and cannot log in. A new login password needs to be generated. |

# 2. Changing the System Password

If you can still log in to the server, it is recommended to change the password directly within the operating system.

## Linux

Applicable when:

- You can log in to the server via SSH.
- You can access the server through VNC.

After changing the password, please log in again using the new password to verify that it has taken effect.

## Windows

Applicable when:

- You can log in to the server via Remote Desktop (RDP).
- You can access the server through VNC.

After changing the password, please log in again using the new password to verify that it has taken effect.

**Note:** The password change procedure may vary depending on the operating system version. Please follow the instructions for your specific operating system.

---

# 3. Resetting the Password Through the Control Panel

If you have forgotten your server password and cannot log in, you can generate a new password using the **Reset Password** feature in the Bare Metal Cloud Control Panel.

## Steps

1. Log in to the Raksmart Client Portal.
2. Navigate to **Product Management** → **Bare Metal Cloud**.
3. Select the server you want to manage.
4. Go to the **Management** page.
5. Click **Reset Password**.
6. The system will automatically generate a new random password.
7. If you would like a different password, click **Regenerate** to generate another random password, or enter your own custom password.
8. Once confirmed, click **Copy** to save the new password.

## After Resetting

Once the new password has been generated, you can use it to log in to your server immediately.

Supported login methods:

- **Linux:** SSH or VNC
- **Windows:** Remote Desktop (RDP) or VNC

**Note:**

The new password takes effect immediately after the reset. No server reboot is required.

---

# 4. When Should You Use VNC?

It is recommended to use VNC to access your server in the following situations:

- SSH connection is unavailable.
- RDP connection is unavailable.
- You cannot confirm whether the server has started successfully.
- Network configuration issues prevent remote access.
- You need to view the server boot process.

**Note:**

VNC provides direct console access to the server. Even if the network connection is unavailable, you can usually still access and manage the system through VNC.

For detailed instructions, please refer to **Bare Metal Cloud VNC Console User Guide**.

---

# 5. Password Security Recommendations

To improve server security, we recommend the following:

- Use a password with at least 12 characters.
- Include uppercase letters, lowercase letters, numbers, and special characters.
- Avoid using easily guessed information such as birthdays or phone numbers.
- Change your password regularly.
- Keep your password secure and do not share it with others.

---

# 6. Frequently Asked Questions

### Q1: Will changing or resetting the password affect my server data?

No.

Changing or resetting the password only updates the login credentials. It does not affect the operating system, applications, or any data stored on the server.

---

### Q2: Do I need to reboot the server after resetting the password?

No.

The new password becomes effective immediately after it is reset through the control panel. A server reboot is not required.

---

### Q3: Why can't I log in after resetting the password?

Please check the following:

- Make sure you are using the most recently generated password.
- Verify that you are using the correct username (for example, **root** for Linux or **Administrator** for Windows).
- Confirm that you are connecting to the correct IP address and port.
- Ensure that the SSH or RDP service is running properly.
- Check whether the Security Group or system firewall is blocking the connection.

If you still cannot log in, try accessing the server through the VNC console for further troubleshooting.

---

### Q4: Can I set my own password when resetting it?

Yes.

The Reset Password feature allows you to either use a randomly generated password or enter your own custom password before completing the reset.

---

### Q5: Will resetting the password reboot my server?

No.

Resetting the password through the control panel does not affect the server's current running status and will not automatically reboot the server.

---

# Notes

⚠️ It is recommended to change the default password immediately after your first login.

⚠️ Before closing the Reset Password window, make sure you have copied or recorded the new password.

⚠️ If your server uses automated management or deployment tools, remember to update the saved password in those tools to avoid authentication failures.

⚠️ If you are unable to log in with the new password for an extended period, please use the VNC console to verify the server status first.

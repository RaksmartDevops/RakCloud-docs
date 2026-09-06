# VPS Cloud Disk User Guide

## Purpose

This document describes the basic operations for VPS Cloud Disks, including creating, attaching, detaching, and deleting a cloud disk. It is intended to help customers quickly understand how to use the Cloud Disk feature.

A Cloud Disk provides additional storage space for your VPS and can be used to expand storage capacity, store business data, or manage data separately from the system disk.

**Applicable Product:**

- VPS (Virtual Private Server)

---

# 1. What Is a Cloud Disk?

A Cloud Disk is an independent storage resource that can be attached to a VPS.

Unlike the system disk, a Cloud Disk is primarily used to store business data and can be attached, detached, or deleted as needed.

**Common use cases include:**

- Expanding server storage capacity
- Storing website files
- Storing database files
- Separating business data from the operating system
- Independent backup of business data

---

# 2. Creating a Cloud Disk

### Steps

1. Log in to the Raksmart Client Portal.
2. Go to **Purchase Center → VPS**.
3. Click **Purchase Cloud Disk**.
4. Select the desired disk capacity, region, and other configuration options based on your requirements.
5. Complete the payment. Once the order is completed, the Cloud Disk will appear in your account.

**Note:**

When purchasing a Cloud Disk, make sure the selected **region** matches the VPS that you intend to attach it to. Otherwise, the Cloud Disk cannot be attached.

---

# 3. Attaching a Cloud Disk

### Steps

1. Log in to the Raksmart Client Portal.
2. Go to **Product Management → VPS → Cloud Disk**.
3. Select the Cloud Disk you want to attach.
4. Click **Mount**.
5. Choose the target VPS from the instance list.
6. Confirm the operation to complete the attachment.

**Notes:**

- A Cloud Disk can only be attached to a VPS located in the **same region**.
- If the target VPS does not appear in the instance list, verify that it is located in the same region as the Cloud Disk.
- Attaching a Cloud Disk **does not reboot the VPS** and **does not interrupt running services**.

---

# 4. What Should I Do After Attaching the Cloud Disk?

After the Cloud Disk is attached through the control panel, the operating system will detect the new disk. However, the disk **will not be automatically partitioned, formatted, or mounted**.

You must log in to the server and complete the following steps according to your operating system:

- Detect the newly attached disk.
- Create disk partitions (if required).
- Create a file system (for first-time use).
- Mount the disk to the desired directory.
- Configure automatic mounting at system startup (if required).

**Note:**

Completing the attachment in the control panel only connects the Cloud Disk to your VPS. The disk must still be initialized and mounted within the operating system before it can be used.

---

# 5. Detaching a Cloud Disk

If you need to remove a Cloud Disk from a VPS, you can detach it through the control panel.

### Steps

1. Log in to the Raksmart Client Portal.
2. Go to **Product Management → VPS → Cloud Disk**.
3. Select the Cloud Disk.
4. Click **Unmount**.
5. Confirm that you want to detach the disk from the server.

**Recommendation:**

Before detaching the Cloud Disk, unmount the file system from within the operating system and ensure that no applications or services are currently using the disk. This helps prevent data inconsistency or file system corruption.

**Note:**

Detaching a Cloud Disk **does not delete the data stored on it**.

---

# 6. Frequently Asked Questions

### Q1: Why can't I find the VPS that I want to attach the Cloud Disk to?

A Cloud Disk can only be attached to a VPS located in the **same region**.

If the target VPS does not appear in the instance list, please verify that both the Cloud Disk and the VPS are located in the same region.

---

### Q2: Will attaching a Cloud Disk reboot my VPS?

No.

Attaching a Cloud Disk through the control panel **does not reboot the VPS** and **does not interrupt your running services**.

---

### Q3: Why can't I use the disk immediately after attaching it?

After the Cloud Disk is attached, you must initialize it within the operating system.

This includes:

- Creating partitions (if required)
- Formatting the disk (first-time use)
- Mounting the file system

The Cloud Disk will be available for use only after these steps have been completed.

---

### Q4: Will detaching a Cloud Disk delete my data?

No.

Detaching a Cloud Disk only removes the association between the disk and the VPS. The data stored on the Cloud Disk remains intact.

---

### Q5:Can I recover my data after a Cloud Disk has been reclaimed?

No.

Once a Cloud Disk has been reclaimed due to expiration, cancellation, refund, or other service termination, the data stored on the disk cannot be recovered.

Please make sure to back up all important data before the Cloud Disk is reclaimed.

---

# Notes

⚠️ A Cloud Disk can only be attached to a VPS in the **same region**. Cross-region attachment is not supported.

⚠️ After attaching a Cloud Disk, you must initialize and mount it within the operating system before it can be used.

⚠️ Attaching or detaching a Cloud Disk **does not reboot the VPS**.

⚠️If a Cloud Disk is reclaimed due to expiration, cancellation, refund, or other service termination, the data stored on the disk cannot be recovered. Please back up all important data in advance to avoid permanent data loss.

---

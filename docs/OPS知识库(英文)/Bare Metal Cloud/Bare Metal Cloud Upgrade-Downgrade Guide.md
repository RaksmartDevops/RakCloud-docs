# Bare Metal Cloud Upgrade/Downgrade Guide

## Purpose

This document explains the procedures and important considerations for upgrading or downgrading your Bare Metal Cloud server configuration, helping you complete configuration changes smoothly.

**Applicable Product:** Bare Metal Cloud

---

# 1. Before You Begin

Before performing an upgrade or downgrade, please read the following important information carefully.

## **1.1 Prerequisites**

- The server must be in the **Paid** status before an upgrade or downgrade can be performed.
- After the upgrade or downgrade is completed, the server will automatically reboot. Please make sure to save your work and back up important data in advance to avoid service interruption or data loss.

## **1.2 Downgrade Refund Policy**

If you downgrade your server configuration during the current billing cycle, **the price difference for the downgraded resources is non-refundable**.

However, the server configuration and renewal price will be updated accordingly after the downgrade.

---

# 2. Upgrade/Downgrade Procedure

## **Step 1: Open the Server Management Page**

1. Log in to the Raksmart Client Area.
2. From the left navigation menu, select **Products** → **Bare Metal Cloud**.
3. Locate the server you wish to upgrade or downgrade (make sure its status is **Paid**).
4. Click the product name to enter the server management page.

---

## **Step 2: Open the Upgrade/Downgrade Page**

1. On the server management page, click **Upgrade/Downgrade**.
2. The system will display the following notice:

> **Notice**
>
> If you downgrade your server configuration during the current billing cycle, the price difference for the downgraded resources is non-refundable. However, your renewal price and configuration will be adjusted accordingly.
>
> For Bare Metal Cloud products, upgrading or downgrading the CPU, memory, or adding/removing Classic Network IP addresses will automatically reboot the server. Please back up your important data before proceeding.

3. After carefully reading the notice, click **Confirm** to enter the configuration page.

---

## **Step 3: Select the Configuration to Change**

On the Upgrade/Downgrade page, you can adjust the following configuration items as needed:

- **Bandwidth** – Select the desired bandwidth.
- **Traffic** – Select the required traffic plan.
- **DDoS Protection** – Available in selected locations only.
- **IP Addresses** – Standard IPs can be increased to a maximum of **64**.
- **Memory (RAM)** – Select the desired memory size.
- **HDD Data Disk** – Increase storage capacity.
- **SSD Data Disk** – Increase storage capacity. HDD and SSD data disks can be used simultaneously.

---

## **Step 4: Confirm and Submit**

1. After selecting the desired configuration, click **Continue**.
2. The system will generate the corresponding invoice(s).
3. **Note:** If you upgrade multiple configuration items at the same time, each item will generate a separate invoice, and each invoice must be paid individually.
4. Once payment is completed, the server will automatically reboot and apply the new configuration.

---

# 3. View the Updated Configuration

After the upgrade or downgrade is completed, you can view the updated server configuration under the **Configuration Options** section on the server management page.

For more details, please refer to the **Configuration Options** section in the [*Bare Metal Cloud Control Panel Guide*](https://billing.raksmart.com/whmcs/index.php?rp=%2Fknowledgebase%2F1152%2F%E8%A3%B8%E6%9C%BA%E4%BA%91%E6%8E%A7%E5%88%B6%E5%8F%B0%E6%93%8D%E4%BD%9C%E6%8C%87%E5%8D%97.html&language=english).

---

# 4. Frequently Asked Questions

## Q1. Why can't I upgrade the CPU?

**A:** The CPU is a core hardware component determined by the physical processor installed in the server and cannot be replaced after purchase.

If you require a more powerful CPU, we recommend purchasing a new server with the desired CPU configuration.

---

## Q2. Why can't I change the network line?

**A:** The network line is part of the server's underlying network architecture and routing configuration and cannot be changed after purchase.

If you need a different network line, please purchase a new server with the required network option.

---

## Q3. Can I receive a refund after downgrading my configuration?

**A:** No.

Downgrading during the current billing cycle does not qualify for a partial refund of the downgraded resources.

However, your renewal price will be adjusted based on the new configuration.

---

## Q4. Will upgrading or downgrading affect my server?

**A:** Yes.

The server will automatically reboot after the upgrade or downgrade is completed.

Please save your work and back up important data before proceeding. We also recommend performing the operation during off-peak hours to minimize service impact.

---

## Q5. Why can't I see a specific configuration option on the Upgrade/Downgrade page?

**A:** If a configuration item is not displayed on the Upgrade/Downgrade page, it means that item does not support upgrades or downgrades.

For example, **CPU**, **system disk**, and **network line** cannot be modified after purchase.

---

## Q6. Can I upgrade a server that is overdue or suspended?

**A:** No.

The server must be in **Paid** status before an upgrade can be performed.

Please renew the server first, then proceed with the upgrade.

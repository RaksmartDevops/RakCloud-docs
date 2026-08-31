# VPS Elastic IP User Guide

## Purpose

This document introduces the features, usage scenarios, and management procedures for VPS Elastic IPs (EIP). It helps users understand how to bind, unbind, and manage Elastic IPs through the Raksmart control panel.

**Applicable Products:**

- VPS (Virtual Private Server)

---

# 1. What is an Elastic IP (EIP)?

An Elastic IP (EIP) is a public IP address that can be managed independently and bound to or unbound from a VPS instance as needed.

Unlike the default public IP assigned to a VPS, an Elastic IP can be managed separately, making it more flexible for server migration and network management.

**Common Use Cases:**

- Assign an additional public IP to a VPS.
- Rebind an existing public IP to another VPS.
- Flexibly manage public IP resources for different business scenarios.

---

# 2. Accessing the Elastic IP Management Page

1. Log in to the Raksmart Client Area.
2. Navigate to:

**Products & Services → VPS  → Elastic IP**

On the Elastic IP management page, you can view all Elastic IPs under your account, including:

- IP Address
- Region
- Network Route
- Status (Bound / Available)
- Associated VPS Instance (if applicable)

---

# 3. Binding an Elastic IP

When an Elastic IP is in the **Available** state, it can be bound to a VPS.

### Steps

1. Log in to the Raksmart Client Area.
2. Go to **Products & Services → VPS → Elastic IP**.
3. Select the Elastic IP you want to use.
4. Click **Allocation**.
5. Select the target VPS instance.
6. Confirm the operation.

After the binding is completed, the VPS will automatically reboot to apply the new network configuration.

> **Note:**
>
> Binding an Elastic IP will automatically restart the VPS. Please ensure that your business can tolerate the temporary service interruption before proceeding.

---

# 4. Unbinding an Elastic IP

If you no longer need an Elastic IP to be associated with the current VPS, you can unbind it.

There are two ways to unbind an Elastic IP.

### Method 1: Unbind from the Elastic IP Page

1. Go to **Products & Services → VPS → Elastic IP**.
2. Locate the bound Elastic IP.
3. Click **Idle**.
4. Confirm the operation.

Once unbound, the Elastic IP will return to the **Available** state and can be bound to another eligible VPS.

> **Note:**
>
> Unbinding an Elastic IP will also automatically restart the VPS.

---

# 5. Binding Requirements

An Elastic IP cannot be bound to any VPS arbitrarily. The following requirements must be met:

- The Elastic IP and the VPS **must be located in the same region**.
- The Elastic IP and the VPS **must use the same network route**.

For example:

- A Los Angeles International BGP Elastic IP can only be bound to a Los Angeles International BGP VPS.
- A Japan Mainland Optimized Elastic IP cannot be bound to a Japan International BGP VPS.

If the VPS does not meet these requirements, it **will not appear in the instance selection list**, and the binding cannot be completed.

---

# 6. Recommended Usage

Elastic IPs are recommended for the following scenarios:

- Flexible public IP management.
- Migrating services to another VPS.
- Retaining the same public IP after replacing a VPS.
- Managing multiple public IP resources.

If your VPS does not require public IP reassignment, you may continue using the default public IP assigned to the instance.

---

# 7. Frequently Asked Questions

### Q1: Why can't I find my VPS when binding an Elastic IP?

This usually occurs because the Elastic IP and the VPS are not in the same **region** or do not use the same **network route**.

Please verify:

- The region matches.
- The network route matches.

Only VPS instances that satisfy both requirements will appear in the binding list.

---

### Q2: Will binding an Elastic IP affect my server?

Yes.

The VPS will automatically reboot after the Elastic IP is bound to apply the new network configuration.

It is recommended to perform this operation during maintenance windows or periods of low business traffic.

---

### Q3: Will unbinding an Elastic IP restart my VPS?

Yes.

The VPS will automatically reboot after the Elastic IP is unbound.

---

### Q4: Will the Elastic IP be released after it is unbound?

No.

After unbinding, the Elastic IP remains under your account and changes to the **Available** state. It can be bound again to another eligible VPS.

---

### Q5: Why can't I access my server after successfully binding an Elastic IP?

Please check the following:

- The VPS has completed the automatic reboot.
- The security group or system firewall allows the required ports.
- SSH (Linux) or RDP (Windows) services are running properly.
- DNS records have been updated if you are accessing the server via a domain name.

---

# Notes

⚠️ The Elastic IP and VPS **must belong to the same region and use the same network route**; otherwise, the binding operation is not supported.

⚠️ If the target VPS does not appear during the binding process, please verify that both the region and network route match.

⚠️ Both **binding and unbinding** an Elastic IP will automatically restart the VPS. Please plan accordingly to avoid service interruptions.

⚠️ Unbinding an Elastic IP does **not** release it. The Elastic IP remains in your account and can be bound again to another eligible VPS.

# VPS Security Group User Guide

## Purpose

This document introduces the basic functions of VPS Security Groups, including how to create, associate, and manage security groups and security rules. It helps customers control network access to their VPS and improve server security.

**Supported Product:**

- VPS (Virtual Private Server)

---

# 1. What Is a Security Group?

A Security Group is a virtual firewall used to control network access to your VPS.

By configuring security group rules, you can control which IP addresses, protocols, and ports are allowed or denied access to your server, helping improve overall network security.

Common use cases include:

- Controlling inbound traffic
- Controlling outbound traffic
- Restricting access from specific IP addresses or IP ranges
- Opening or closing specific service ports
- Enhancing server security

---

# 2. Security Group Overview

When a VPS is created, the system automatically associates it with a default Security Group.

The default Security Group usually allows the basic remote access ports required to manage your server, including:

- SSH (Port 22)
- Windows Remote Desktop (RDP, Port 3389)
- ICMP (Ping)

Therefore, in most cases, you can connect to your server immediately after deployment.

**Notes:**

- Each VPS can be associated with one Security Group.
- Multiple Security Groups can be created within the same region.
- One Security Group can be designated as the default Security Group for each region.
- An associated Security Group can be detached or replaced at any time.

---

# 3. Security Group Management

The platform provides two methods for managing Security Groups.

---

## Method 1: From the VPS Management Page (Recommended)

This method is suitable for managing the Security Group of a specific VPS.

**Navigation:**

**Product Management → VPS → Security Group**

Available operations include:

- Enable Security Group
- Disable Security Group
- Create a Security Group
- Associate a Security Group
- Remove a Security Group Association
- Manage Security Group Rules
- Delete a Security Group

This method is recommended when managing the network policy of an individual VPS.

---

## Method 2: Global Security Group Management

This method is suitable for centrally managing all Security Groups within the same region.

**Navigation:**

**Product Management → VPS → Security Group**

You can switch between different regions, such as:

- Hong Kong
- Japan
- Taiwan
- Korea
- Malaysia
- Singapore
- Silicon Valley
- Los Angeles
- Seattle

Available operations include:

- Create Security Groups
- Edit Security Groups
- Delete Security Groups
- Set the Default Security Group
- Manage Security Group Rules

This method is recommended for customers managing multiple VPS instances within the same region.

---

# 4. Creating a Security Group

Click **Add** to create a new Security Group.

When creating a Security Group, you need to specify:

- Security Group Name
- Whether to set it as the Default Security Group

After creation, the Security Group can be associated with one or more VPS instances.

---

# 5. Associating or Removing a Security Group

On the VPS Security Group page, you can associate an existing Security Group with your VPS.

Supported operations include:

### Apply

Associates the selected Security Group with the current VPS.

### Remove

Removes the Security Group association from the current VPS.

**Note:**

After removing the Security Group, the VPS will no longer be protected by its security rules. Ensure that appropriate firewall policies are configured within the operating system to avoid exposing your server to unnecessary security risks.

---

# 6. Managing Security Group Rules

Within the Security Group management page, you can add, edit, or delete security rules.

---

## Adding a Security Rule

Click **Add** and configure the following parameters:

| Parameter | Description |
| --- | --- |
| Remote IP | The source IP address or CIDR block to allow or deny. For example, `0.0.0.0/0` allows access from all IP addresses. |
| Direction | Inbound or Outbound |
| Protocol | TCP, UDP, ICMP, etc. |
| Minimum Port | Starting port number |
| Maximum Port | Ending port number |

**Notes:**

- For a single port, set the minimum and maximum port to the same value (for example, **22–22**).
- To allow a range of ports, specify the desired port range (for example, **8000–8080**).
- Protocols such as ICMP do not require port numbers.

---

## Editing a Security Rule

Click **Edit** to modify an existing rule.

You can update:

- Remote IP
- Protocol
- Direction
- Port Range

---

## Deleting a Security Rule

Click **Delete** to remove a security rule.

**Note:**

After a rule is deleted, the corresponding network access will no longer be permitted according to that rule. Please ensure that removing the rule will not affect your services.

---

# 7. Common Use Cases

## Scenario 1: Opening Website Ports

After deploying a website, add inbound rules for:

- TCP Port 80 (HTTP)
- TCP Port 443 (HTTPS)

This allows users to access your website normally.

---

## Scenario 2: Allowing SSH Access

Linux servers typically use:

- TCP Port 22

If you change the SSH port, remember to update the Security Group accordingly.

---

## Scenario 3: Allowing Windows Remote Desktop

Windows servers typically use:

- TCP Port 3389

If the Remote Desktop port has been changed, update the Security Group rules to match.

---

## Scenario 4: Using aaPanel

After installing **aaPanel**, you must also allow the required ports in the Security Group; otherwise, the panel will not be accessible.

Common ports include:

- 8888 (aaPanel)
- 80 (HTTP)
- 443 (HTTPS)

Open additional ports as required by your services.

---

# 8. Frequently Asked Questions

### Q1: What happens if I disable the Security Group?

Once the Security Group is disabled, the platform will no longer filter network traffic for your VPS.

It is recommended that you configure the operating system firewall to maintain proper security.

---

### Q2: Why can't I access a service after opening the port?

Please verify the following:

- The Security Group allows the required port.
- The operating system firewall allows the connection.
- The service is running properly.
- The service is listening on the correct port.

---

### Q3: Can one VPS be associated with multiple Security Groups?

Currently, each VPS supports association with **one Security Group only**.

---

### Q4: Can Security Groups restrict access to specific IP addresses?

Yes.

You can configure the **Remote IP** field to allow access only from specific IP addresses or CIDR ranges.

---

# Notes

⚠️ Security Groups are used to control network access to your VPS. Configure security rules carefully according to your business requirements.

⚠️ Modifying or deleting Security Group rules may affect the accessibility of your services. Verify the impact before making changes.

⚠️ If you change the listening port of a service, remember to update the corresponding Security Group rule.

⚠️ After deploying websites, databases, aaPanel, or other applications, make sure the required service ports are allowed in the Security Group; otherwise, the services may not be accessible.

# Bare Metal Cloud Monitoring Feature Guide

## Purpose

This document explains how to use the monitoring feature in the Bare Metal Cloud Control Panel, including monitoring metrics, historical data viewing, and frequently asked questions. It helps you monitor your server's resource usage in real time and assists with daily operations and troubleshooting.

**Applicable Product:** Bare Metal Cloud

---

# 1. Monitoring Feature Overview

The Bare Metal Cloud Control Panel provides built-in monitoring to help you view your server's resource usage and historical performance trends.

The monitoring page allows you to quickly understand the current operating status of your server and analyze historical resource usage for performance optimization and troubleshooting.

The following monitoring metrics are currently available:

- CPU Usage
- Memory Usage
- Disk I/O
- Network Traffic
- Resource Usage Charts

You can also view historical monitoring data by selecting a specific date and time range.

---

# 2. How to View Monitoring Information

1. Log in to the **Raksmart Client Portal**.
2. Navigate to **Product Management** → **Bare Metal Cloud**.
3. Select the server you want to monitor.
4. Open the **Management** page.
5. Click **Monitor**.

The monitoring page will display the server's resource usage and performance statistics.

---

# 3. Monitoring Metrics

## CPU Usage

CPU Usage indicates how much processor resource is currently being utilized.

Consistently high CPU usage may indicate:

- High server workload
- CPU-intensive applications
- Abnormal or resource-consuming processes

---

## Memory Usage

Memory Usage shows the amount of system memory currently in use.

If memory usage remains close to full capacity for an extended period, it may result in:

- Slow system performance
- Reduced application responsiveness
- Service interruptions

If necessary, consider optimizing applications or upgrading server resources.

---

## Disk I/O

Disk I/O reflects the server's disk read and write activity.

Consistently high Disk I/O may indicate:

- Heavy file read/write operations
- Frequent database activity
- Backup or synchronization tasks
- High disk workload

---

## Network Traffic

Network Traffic displays the amount of data transmitted through the server's network interface.

It can be used to monitor:

- Network traffic trends
- Business traffic patterns
- Upload and download activity

If network traffic increases significantly within a short period, it is recommended to verify whether the activity is expected.

---

## Resource Usage Charts

The monitoring page provides graphical charts showing historical resource usage over time.

You can select different dates and time ranges to review historical monitoring data, making it easier to analyze performance trends and identify when issues occurred.

---

# 4. How to Identify Potential Issues

Monitoring data can help you quickly determine whether your server is experiencing abnormal resource usage.

Common examples include:

> |  |  |
> | --- | --- |
> | Monitoring Observation | Possible Cause |
> | CPU usage remains consistently high | High workload, resource-intensive applications, or abnormal processes |
> | Memory usage stays close to full capacity | Insufficient memory, high application usage, or memory leaks |
> | Disk I/O remains consistently high | Heavy disk operations, frequent database activity, or backup tasks |
> | Sudden increase in network traffic | Increased business traffic, file transfers, data synchronization, or abnormal network activity |
> | Resource usage remains significantly higher than usual | Further investigation using system logs and application status is recommended |
>
> **Note:**
>
> Monitoring data reflects the server's resource usage only. Determining the root cause of an issue may require reviewing system logs, application status, and server configuration.

---

# 5. Viewing Historical Monitoring Data

The monitoring feature allows you to review historical resource usage.

You can select a specific date and time range to view server performance during a particular period.

Historical monitoring data can be used to:

- Analyze server performance trends
- Identify when an issue occurred
- Compare resource usage over time
- Assist in troubleshooting performance-related problems

---

# 6. Frequently Asked Questions

### Q1: Is the monitoring data updated in real time?

Monitoring data is collected at regular intervals, so a short delay may occur before the latest information is displayed.

---

### Q2: Does high CPU usage indicate a server failure?

Not necessarily.

High CPU usage may simply indicate increased business traffic, running applications, or scheduled system tasks.

It is recommended to analyze CPU usage together with system processes and application activity.

---

### Q3: Why has my network traffic suddenly increased?

Possible reasons include:

- Increased website traffic
- File uploads or downloads
- Data synchronization
- Software updates
- Abnormal network activity

Please review your server logs and running services to determine the cause.

---

### Q4: The monitoring data looks normal, but my server is still inaccessible. What should I do?

Monitoring data reflects only the server's resource usage.

If the server cannot be accessed, please also check:

- Network connectivity
- Security Group rules
- Firewall configuration
- SSH or Remote Desktop (RDP) services
- Application status

If necessary, use the **VNC Console** or **Rescue Mode** for further troubleshooting.

---

# Notes

⚠️ Monitoring data is intended to provide an overview of server resource usage and should not be used as the sole indicator of server health.

⚠️ It is recommended to regularly monitor CPU, Memory, Disk I/O, and Network Traffic to identify potential issues early.

⚠️ Historical monitoring data can be viewed by selecting a specific date and time range, making it easier to analyze resource usage trends and troubleshoot problems.

⚠️ If server resources remain under heavy load for an extended period, consider optimizing your applications or upgrading your server configuration.

---

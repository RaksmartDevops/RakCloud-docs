# VPS Monitoring Features Guide

## Purpose

This document introduces the monitoring and usage statistics features available in the VPS control panel. It helps customers monitor server performance, resource utilization, and network traffic for daily operations and performance analysis.

**Supported Product:**

- VPS

---

# 1. Accessing the Monitoring Page

### Steps

1. Log in to the **Raksmart Client Portal**.
2. Go to **Product Management → VPS**.
3. Select the VPS you want to manage.
4. Enter the VPS management page.
5. By default, you will be taken to the **Charts** (Monitoring) page.

The following tabs are available:

- Charts
- Usage

---

# 2. Charts (Real-Time Monitoring)

The **Charts** page provides real-time monitoring of your VPS resources, allowing you to view the current operating status of your server.

The following monitoring metrics are available:

- CPU Usage
- Disk I/O
- Memory Usage
- Network Traffic

These charts help you determine whether:

- CPU utilization remains consistently high.
- There is abnormal disk read/write activity.
- Memory resources are insufficient.
- Network traffic is unusually high.

**Note:**

Monitoring data is updated continuously and can be used for daily performance monitoring and troubleshooting.

---

## CPU Usage

Displays the current CPU utilization of the VPS.

Typical use cases include:

- Monitoring long-term CPU usage.
- Identifying processes consuming excessive CPU resources.
- Analyzing CPU usage during peak business hours.

---

## Disk I/O

Displays disk read and write activity.

You can select different disks (such as the system disk or data disk) for monitoring.

Typical use cases include:

- Monitoring disk I/O performance.
- Identifying unusually high disk activity.
- Troubleshooting performance issues caused by disk operations.

---

## Memory Usage

Displays the current memory usage of the VPS.

Typical use cases include:

- Monitoring memory consumption.
- Determining whether memory resources are sufficient.
- Analyzing memory usage trends over time.

---

## Network Traffic

Displays the real-time network traffic of the VPS.

You can monitor the incoming and outgoing traffic of the network interface.

Typical use cases include:

- Monitoring current network usage.
- Analyzing business traffic.
- Identifying abnormal network activity.

---

# 3. Usage Statistics

The **Usage** page displays historical network traffic statistics for your VPS.

The page supports:

- Viewing historical traffic usage.
- Selecting a specific time range.
- Customizing the start and end dates for traffic statistics.

Customers can review network traffic usage over a selected period to better understand bandwidth consumption and traffic trends.

**Note:**

The Usage page is intended for network traffic statistics. Depending on the selected time range, there may be a slight delay before the latest data is displayed.

---

# 4. Frequently Asked Questions

### Q1: Why is there no data displayed in the monitoring charts?

Please check the following:

- Whether the VPS is running normally.
- Whether sufficient time has been allowed for monitoring data to be collected.
- Whether the correct monitoring item has been selected.

If the VPS has just been created or restarted, monitoring data may take some time to appear.

---

### Q2: What should I do if CPU usage remains high?

Log in to your VPS and check:

- Whether any applications are consuming excessive CPU resources.
- Whether there are abnormal processes running.
- Whether scheduled tasks are continuously using CPU resources.

If the high CPU usage is caused by normal business workloads, consider upgrading your VPS configuration.

---

### Q3: Why is memory usage very high?

High memory usage does not necessarily indicate a problem.

Linux systems commonly use available memory as file cache. It is recommended to evaluate memory usage together with available memory and your actual workload.

---

### Q4: Why is Disk I/O continuously high?

Possible causes include:

- Frequent database read/write operations.
- Large file transfers.
- Applications performing continuous disk operations.

It is recommended to log in to the server for further investigation.

---

### Q5: Can I view historical traffic statistics?

Yes.

The **Usage** page allows you to select a custom date range and view network traffic statistics for the selected period.

---

# Notes

⚠️ Monitoring data is intended to reflect server resource utilization and does not necessarily indicate a system issue.

⚠️ If the VPS has just been created, restarted, or restored, monitoring data may take some time to become available.

⚠️ The **Usage** page supports custom date range queries, allowing you to review historical traffic statistics as needed.

⚠️ If CPU usage, memory usage, disk I/O, or network traffic remains abnormally high for an extended period, it is recommended to first inspect the server and running applications before considering resource optimization or a VPS upgrade.

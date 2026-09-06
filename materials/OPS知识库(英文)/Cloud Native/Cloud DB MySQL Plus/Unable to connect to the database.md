# Unable to connect to the database

In actual business scenarios, there may be situations where you are unable to connect to MySQL Plus. You can refer to the following troubleshooting steps to perform a self-check, or you can directly raise a support ticket to contact technical support.

## Troubleshooting cluster status

Methods of troubleshooting

1. Check the running status of the target cluster on the AppCenter cluster management page to verify if it is active.
2. Check the resource status of the cluster nodes and verify if the disk usage rate has exceeded 85% and if there is insufficient disk space.
3. Check the instance connection count and review all service metrics, including the total connection count. Verify the maximum connection count of the cluster to determine if the connection count is too high.

   -The `max\_connections` parameter represents the maximum number of concurrent client connections allowed. If the value is set to "default," it means the maximum connection -

   -The `max\_user\_connections` parameter refers to the maximum number of concurrent connections allowed for a specific MySQL account.

**Possible reasons.**

1. Possible reasons: MySQL Plus system failure, abnormal status, and cluster or table being locked.
2. Possible reason: When the disk usage of the database exceeds 85%, the database may become unavailable and unable to perform normal operations such as connection and write operations.
3. Possible reason: If the database connection limit is reached, it can cause the inability to establish new connections, resulting in the inability of the business to connect properly. It can also lead to failure in performing full and incremental backups, which can impact the normal operation of the business.

**Solution:**

1. Select the target cluster, choose "More Actions" > "Restart" to attempt restarting the database.
2. Expand the cluster's disk space to increase available storage; delete expired data; shorten the retention period of binlog; enable monitoring and alerts for CPU, memory, disk, and other resource metrics to stay informed about the cluster's resource status in a timely manner.
3. Investigate if the business connections are valid and release idle connections; set "default" and expand the cluster's memory space to increase the max\_connections value; enable monitoring and alerts for current thread connections and other service metrics to stay informed about the cluster's service status in a timely manner.

## Troubleshoot the connection method.

Troubleshooting methods.

1. Check if the installed MySQL client version is lower than the MySQL version of the cluster.
2. Log in to the AppCenter cluster management page and check if the target cluster has enabled SSL encrypted transmission. Also, verify if the user account has enabled encryption authentication.
3. Check if the connection command is correct.
4. Check if the connection user account is correctly authorized or has been deleted in the cluster account list.

Possible reasons

1. The MySQL client version is lower than the MySQL version of the cluster, causing compatibility issues and preventing a successful connection.
2. After enabling SSL encrypted transmission for the cluster, the user account may not have enabled SSL authentication, or the SSL certificate may not have been uploaded correctly, or the connection command may be incomplete.
3. The connection command is not correct.
4. The user account is not authorized as '%', or the user account has been deleted and is not available for connection.

Possible solutions

1. Confirm the database kernel version and choose the corresponding version of the MySQL client to install.
2. Enable SSL encryption for the cluster and enable encryption authentication for the database accounts. Also, make sure to upload the SSL certificate to the server.
3. Retrieve the correct connection address, port configuration, user account, password, and SSL certificate name. Retry the connection to the instance using these updated parameters.
4. Modify the user account authorization to '%', re-add the user account, and retrieve the user account and password for connection.

Example of correct connection method:

- After enabling SSL encrypted transmission, connect using the public IP address：`mysql -h <外网地址> -P 3306 -u testuser -p --ssl-ca=ca.pem --ssl-cert=client-cert.pem --ssl-key=client-key.pem`
- After enabling SSL encrypted transmission, connect using the internal IP address：`mysql -h <外网地址> -P 3306 -u testuser -p --ssl-ca=ca.pem --ssl-cert=client-cert.pem --ssl-key=client-key.pem`

> Note
>
> The SSL certificate file needs to be uploaded to the server and placed in the directory where the connection command is executed.

## Troubleshooting network issues

### Internal network address connection

**Troubleshooting methods**

1. Please check if the cloud server and the target MySQL Plus cluster are in the same region and the same VPC network.
2. Check the security group rules associated with the cloud server.
3. Use the command "telnet <internal IP address> <port>" to check if the current cloud server can successfully connect to the database port.

**Possible Cause**

1. Network isolation between cloud resources in different regions or VPC networks, preventing connectivity.
2. Cloud server's associated security group does not allow outbound access to the target cluster.
3. Cloud server is unable to access the open ports of the cluster.

**Solution**

1. Based on the proximity principle, you can migrate the database resources or purchase a new cloud server to ensure they are within the same VPC network. Utilize VPC network's tunneling services and VPN services to establish connectivity between resources located in different regions or VPCs.
2. Add inbound rules to the cloud server's security group to allow access to the target cluster.
3. If the cloud server cannot connect to the target database port, please submit a ticket to contact technical support.

### External IP Address Connection

**Troubleshooting Method**

1. Adding 0.0.0.0/0 to the IP whitelist and checking if the connection can be established.
2. Checking the associated security group rules of the cloud server.
3. Checking the network ACL rules associated with the cloud server subnet.
4. Perform a ping test from a cloud server in the same region to validate the connectivity to the cluster IP.

Possible reasons

1. External server IP address changes, causing incorrect configuration in the whitelist.
2. The cloud server's associated security group does not allow access to the target cluster.
3. The private network bound to the cloud server has a network ACL enabled, but it is not configured to allow access to the target cluster.
4. The VPC networks within the region are not interconnected.

Solution

1. Verify the connection after adding 0.0.0.0/0 to the whitelist.

   -If the connection is successful, on the client where the connection was established, execute the command "show processlist" to retrieve the process information. Look for the correct IP address in the "Host" column and add it to the whitelist.

   -If the connection is not successful, please investigate other possible causes.

   > Explanation
   >
   > 0.0.0.0/0 represents allowing any server to connect to the database. After verification, it is recommended to promptly remove the configuration from the whitelist.
2. Add an outbound rule to the current cloud server security group to allow access to the target cluster.
3. Disable the private network of the cloud server; add an outbound rule to the enabled network ACL to allow network access to the target cluster.
4. If the cloud server in the same region cannot ping the cluster, please submit a support ticket to contact technical support.

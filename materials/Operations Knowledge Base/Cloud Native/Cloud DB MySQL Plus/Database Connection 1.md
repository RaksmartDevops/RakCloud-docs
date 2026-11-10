# Database Connection 1

## 1.Is the IP whitelist effective immediately after being set?

No, it is not. After setting the IP whitelist, it may take a few minutes to take effect.

If it does not take effect after a long time, please submit a ticket to contact technical support for further investigation.

## 2.Do I need to configure a security group after applying for a public IP address?

No, it is not necessary.

To ensure the security of external access, the MySQL Plus service maintains the external security group. The system automatically allows inbound traffic based on the external port, and users do not need to configure or manage security group rules separately.

- When applying for an external IP address, the cluster will automatically bind to an external security group, and the system will automatically allow inbound traffic based on the external port (default 3306) by default. There is no need for separate configuration.
- If the external port or IP whitelist is modified, the external security group associated with the cluster will automatically update its security group rules. There is no need for separate management.

## 3.Does it support cross-region access to the database?

- Internal Access: Cross-region access to the database is not supported. There is no internal network connectivity between cloud resources in different regions, and network connections need to be established.
- External Access: After applying for a public IP address, you can add the public IP address of the cross-region cloud server to the IP whitelist. This allows you to access the database across regions using the public IP address.

## 4.How to determine the public IP address of a local device?

To avoid any issues with the IP whitelist configuration that may result in being unable to access the database, this section introduces several methods to obtain the public IP address of a local device.

- Querying through a web browser

  You can enter any of the following addresses in your web browser to query your public IP address:

  <https://www.cip.cc/>

  <https://www.ipip.net/>
- Query through the command line.

  Execute any of the following commands to obtain your public IP address.

  ```
   # UNIX/Linux 
   $ curl httpbin.org/ip
   $ curl cip.cc
   $ curl ifconfig.io
   $ curl myip.ipip.net
     
   # Windows
   >telnet cip.cc
   >ftp cip.cc
  ```

## 5.Why can't I access through the Proxy node after adding an account?

In the presence of a Proxy, the Proxy node is unaware of the newly added account. To make the Proxy node aware of the newly created account, you need to restart the Proxy node.

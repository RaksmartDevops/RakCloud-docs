# Database Connection 2

MySQL Plus supports connecting to databases using both internal and external IP addresses. It is recommended to use the internal IP address for database connections to ensure data transmission speed while prioritizing data security.

This section provides instructions on how to connect to a MySQL Plus database using the command line interface.

## Connection Methods.

- Internal Network Address Connection: Connect to MySQL Plus using the internal network address. Use the internal network address of the cloud server to establish a direct connection to the cloud database. Connecting via the internal network provides fast network speed and low latency.

  The internal network connection address is provided by the system by default and can be viewed in the MySQL Plus connection information module.

> Note:
>
> -The cloud server and the database must be under the same account and either within the same VPC or in the same basic network.
>
> -For cloud servers and databases located in different VPCs (including same account/different account, same region/different region), you can establish connectivity between them by using VPC peering or VPN services, which provide tunneling capabilities over the VPC network. This allows communication between the cloud servers and databases across different VPCs.

External IP address connection: If you are unable to connect to MySQL Plus using the internal IP address, you can use the external IP address to connect to the database.

To connect to MySQL Plus using the external IP address, you need to manually apply for an external IP address and then check it in the MySQL Plus connection information module.

      Manually apply：<https://docsv3.qingcloud.com/database/mysql/manual/mgt_connect/enable_external_network/>

You can release the external IP address when you don't need to connect to the database using the external IP address.

      Release the public IP address：<https://docsv3.qingcloud.com/database/mysql/manual/mgt_connect/mgt_external_network/>

## Prerequisite conditions.

- The MySQL Plus cluster has been created and the cluster status is active.
- The database login credentials have been created and obtained. For detailed instructions, please refer to Step 2: Create Database Account.

    Create a database account：<https://docsv3.qingcloud.com/database/mysql/quickstart/create_account/>

   If connecting via the public IP address, the account needs to be configured with the authorized host set to '%'.

     Connection via public network address：<https://docsv3.qingcloud.com/database/mysql/manual/mgt_connect/enable_external_network/>

- MySQL client has been installed on the server.

## Retrieve connection information.

1. Click on the target cluster ID in the cluster management page to access the cluster details page.
2. Access the database.

   > Note
   >
   > For a single-node cluster, there is only one node, and the high availability (HA) IP is not displayed in the connection information. You can obtain the IP address of the node in the node list.
   >
   > If you have not created a proxy instance node, the high availability (HA) proxy IP will not be able to establish a connection.

## Accessing the database

Access the database using the obtained database user account and connection information.

Database user account：<https://docsv3.qingcloud.com/database/mysql/quickstart/create_account/>

**Command line connection method is as follows:**

```
mysql -h <mysqlServerName> -P <port> -u <userName> -p -D <databaseName> -ssl-ca=<caNme> --ssl-cert=<> 
```

| Options | Explanation | Example |
| --- | --- | --- |
| -h | Database Internal or External Network Connection Address. | - 192.168.00.00 - gz-cdb-xx123xx.mysql.rakcloud.link |
| -P | Database Port Number. | 3306 |
| -u | Username for the account. | test\_mysql |
| -p | Password for the account.   - To ensure password security, it is common to use the "-p" option for an empty password. After executing the command, you can enter the password and press Enter. - If you need to provide a password, please note that there should be no space between the "-p" option and the password. | test\_mysql |
| -D | Database name. This is an optional parameter; you can omit the "-D" option and only provide the database name. | mysql |
| –ssl- | After enabling SSL encryption for the database, certain connection parameters become mandatory. Please note that the SSL certificate files need to be uploaded to the server and placed in the same directory as the connection command. | –ssl-ca=ca.pem –ssl-cert=client-cert.pem –ssl-key=client-key.pem |

**A successful connection will display something like the following example:**

```
$ mysql -h gz-cdb-xx123xx.mysql.rakcloud.link -P <3306> -u test_mysql -p
Enter password：
Welcome to the MySQL monitor.   Commands end with ; or \g.
Your MySQL connection id is 20
Server version: 8.0.24 Source distribution

Copyright (c) 2000, 2021, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its affiliates. Other names may be trademark of their respective owners.

Type 'help;' or'\h' for help. Type '\c' to clear the current input statement.

mysql>
```

##

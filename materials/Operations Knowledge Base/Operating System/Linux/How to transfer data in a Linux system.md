# How to transfer data in a Linux system

The `scp` command is used for remote file copying in Linux. It allows copying files or directories between multiple Linux systems, similar to the functionality of the *`cp`* command. But instead of local copying, it operates to another host over the network.

Syntax format: scp [parameters] file\_or\_directory [remote\_server\_info]

Common parameters:

-1：Use SSH protocol version 1；

-2：Use SSH protocol version 2；

-4：Use ipv4；

-6：Use ipv6；

-B：Run in batch mode；

-C：Use compression；

-F：Specify the SSH configuration file；

-i：identity\_file Read the key file used for the transfer from the specified file (e.g., Amazon Cloud `.pem` file); this parameter is passed directly to SSH；

-l：Specify bandwidth limit；

-o：Specify the SSH options to use；

-P：Specify the port of the remote host；

-p：Preserve the file's last modification time, last access time, and permission mode；

-q：Do not display the copy progress；

-r：Copy recursively。

 

**Parameters**

- Source file: Specify the source file to be copied.
- Destination file: The target file. The format is *user@host:filename* (where filename is the name of the target file).

 

Example

The scp command to copy from remote to local is similar to the one above; you just need to swap the order of the last two parameters.

**1.Copy files from a remote machine to the local directory**

scp root@10.10.10.10:/opt/soft/nginx-0.5.38.tar.gz /opt/soft/

Download the *`nginx-0.5.38.tar.gz`* file from the *`/opt/soft/`* directory on the machine `10.10.10.10` to the local *`/opt/soft/`* directory.

**2.Copy OpenVPN from Amazon Cloud to the local directory**

scp -i amazon.pem ubuntu@10.10.10.10:/usr/local/openvpn\_as/etc/exe/openvpn-connect-2.1.3.110.dmg openvpn-connect-2.1.3.110.dmg

Download the OpenVPN installation file from the machine `10.10.10.10` to the current local directory.

**3.Copy from a remote machine to the local machine**

scp -r root@10.10.10.10:/opt/soft/mongodb /opt/soft/

Download the *`mongodb`* directory from *`/opt/soft/`* on the machine `10.10.10.10` to the local *`/opt/soft/`* directory.

**4.Upload a local file to a specified directory on a remote machine.**

scp /opt/soft/nginx-0.5.38.tar.gz root@10.10.10.10:/opt/soft/scptest

# Specify the port 2222

scp -rp -P 2222 /opt/soft/nginx-0.5.38.tar.gz root@10.10.10.10:/opt/soft/scptest

Copy the *`nginx-0.5.38.tar.gz`* file from the local *`/opt/soft/`* directory to the *`/opt/soft/scptest`* directory on the remote machine `10.10.10.10`.

**5.Upload a local directory to a specified one on a remote machine.**

scp -r /opt/soft/mongodb root@10.10.10.10:/opt/soft/scptest

Upload the local directory *`/opt/soft/mongodb`* to the *`/opt/soft/scptest`* directory on the remote machine `10.10.10.10`.

# Mounting and Expanding Linux System Disk

For scenarios where additional hard disks need to be added to a machine and manually mounted and expanded Data is invaluable, so ensure that data is backed up before performing any formatting operations.

**一、****Mounting a New Partition**

- #lsblk #View the currently recognized disks in the system and take note of the new disk's name.

![](./images/861db5454e637cf5.png)

- #fdisk    /dev/sdb    #Start partitioning.

n - Create a new partition - Partition type: Press Enter (default) - Partition number: Press Enter (default) - Start sector: Press Enter (default) - Last sector: + Partition size

p - View partition table

w - Save and exit

![](./images/0712cc9777d17156.png)

- # lsblk or fdisk -l - View partition results

![](./images/d0cb01335ede0236.png)

 

- parted /dev/device\_file
- mklabel - Create a partition table
- gpt - We should use the gpt partition table format for disks larger than 2TB
- yes - Confirm that the existing data on the disk will be destroyed
- mkpart - Perform the partition operation, specifying the partition name, file system, and the start and end positions of the partition
- print - Print the partition information

![](./images/efc4cc901f0e1d63.png)

- # mkfs.xfs   -f   /dev/sdb1    #Format the file system as XFS

![](./images/ce43dddb41af5cca.png)

- # blkid   /dev/sdb1      #View the file system type and UUID

![图片3](./images/fa5c31cbba7f8079.png)

- # mkdir  /mypart  #Create a mount point.

- # vim    /etc/fstab   #Set up automatic mounting at startup.

UUID=[File system UUID]   /mypart    xfs    defaults   0   0

![图片4](./images/3119ee99548c5ac7.png)

- # mount   -a       # Refresh or reload the /etc/fstab file

Check if the /etc/fstab file has the correct format for automatic mounting during startup.

Check if the entries in /etc/fstab are written correctly,

- # df  -h

![图片5](./images/83666dd29bb88747.png) 

After executing the reboot command, if there are no issues with the mounted points, it indicates that automatic mounting during startup is effective.

**二****、****Expanding existing partitions.**

Here, we will take /www partition as an example for expanding:

First, verify if your hard disk is part of an LVM volume group. If your machine does not have an LVM volume group, then your hard disk does not support expansion.

- # lsblk  #Check the hard disks recognized by the current system and take note of their current capacities.

![图片1](./images/6a31e1c005a9452f.png)

- # pvdisplay   #Check the volume group names.

![图片3](./images/07c2b69aa594d0d9.png)

- #parted /dev/sda    print   #Display the current disk partitions and check if the format is GPT. Remember the current parameters.

![图片4](./images/b436d92f95ba9e51.png)

If you encounter the error shown in the screenshot, follow the system prompt and enter "Fix". The system will automatically set the capacity of the expanded disk partition to GPT.

![378061be-5fb1-4c27-9c01-14063d62badd](./images/42dfe263f25bbe54.png) 

mkpart primary 1075MB 250GB  #The first 1075MB represents the End capacity mentioned in the second step, and the second 250GB represents the capacity of Disk /dev/sdb.

After completing the process, you can exit by typing "quit".

- # df -h        #You can view the partition results, and here we can see that the partitioning has been successful.

![图片5](./images/cef53288604fdb11.png)

Add the partition to the volume group

- # pvcreate   /dev/sda2  #Add the partition to the physical volume

- # vgextend   vg   /dev/sda2  #Extend the volume group (VG)

- # lvextend  -l  +100%free  /dev/vg/www  #Extend the logical volume (LV)

Format the file system

- # blkid  #Check the file system of the partition to be expanded.

![图片6](./images/d447b5fee231cc28.png)

The command "xfs\_growfs" is used to expand the XFS file system, while "resize2fs" is used to expand the ext4 file system.

- #resize2fs   /dev/vg/www  #Format as ext4

- # df -h  #Here we can see that the expansion has been successful.

![图片7](./images/d4852966170674ea.png)

# reboot  Finally, restart the system and confirm again

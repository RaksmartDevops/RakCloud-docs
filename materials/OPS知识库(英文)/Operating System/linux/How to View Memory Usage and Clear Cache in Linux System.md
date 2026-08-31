# How to View Memory Usage and Clear Cache in Linux System

Sometimes, when a server becomes unresponsive, it may not necessarily be due to high CPU usage. It could also be caused by insufficient memory. You can refer to the following methods to check the memory usage and clear it if necessary.

1.To check the usage of physical memory and swap space on a server, you can use the command: `free -h`.

![](./images/03ae69ccbf56f711.png)

- - total: Total physical memory on the machine.
- - used: Amount of memory currently in use.
- - free: Amount of free (unused) physical memory.
- - shared: Amount of memory shared by multiple processes.
- - buff/cache: Memory used for file system buffers and cache.
- - available: Estimated amount of memory that can be allocated to applications. This is calculated as free + buffer + cache (Note: This calculation is an approximation and may have some margin of error).

2.The command to clear cache is:

echo 1 > /proc/sys/vm/drop\_caches       //To release page cache

![](./images/5a76eaa1334ad7f4.png)

echo 2 > /proc/sys/vm/drop\_caches       //To release dentries (directory cache) and inodes cache

![](./images/afefc3f8cdbdbf9d.png)

echo 3 > /proc/sys/vm/drop\_caches       //To release page cache, dentries (directory cache), and inodes cache

![](./images/32dec15fea0fb436.png)

Note: `echo $?` returns the execution result, where a return value of 0 indicates success.

- - `echo 0` does not release the cache.
- - `echo 1` releases the page cache (clears the cache of recently accessed file pages).
- - `echo 2` releases the dentries (directory cache) and inodes cache (clears the cache of directory entries and file nodes).
- - `echo 3` releases all caches mentioned in options 1 and 2.

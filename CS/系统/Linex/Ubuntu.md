基于[[Linex]]内核的操作系统，他们之间有大部分常用命令的重叠`ls`、`cd`、`pwd`、`mkdir`、`rm`、`cp`、`mv`等，但两者之间也存在一些差异，Ubuntu使用APT作为其包管理器，而其他Linux发行版可能使用不同的包管理器，如Yum或DNF‌。
挂载共享文件夹
sudo mount -t fuse.vmhgfs-fuse .host:/ /mnt/hgfs -o allow_other

```undefined
查看正在运行的gun端口号
sudo lsof -iTCP -sTCP:LISTEN -P | grep gunicorn
关闭程序
sudo kill -9 4004

```


clash
```
启动
./clash -d .
```
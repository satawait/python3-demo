import psutil

print(psutil.cpu_count()) # CPU逻辑数量

print(psutil.cpu_count(logical=False)) # CPU物理核心

print(psutil.cpu_times())

for x in range(10):
    print(psutil.cpu_percent(interval=1, percpu=True))

print(psutil.virtual_memory())

print(psutil.swap_memory())

print(psutil.disk_partitions()) # 磁盘分区信息

print(psutil.disk_usage('/')) # 磁盘使用情况

print(psutil.disk_io_counters()) # 磁盘IOpsutil.disk_io_counters() # 磁盘IO

print(psutil.net_io_counters()) # 获取网络读写字节／包的个数

print(psutil.net_if_addrs()) # 获取网络接口信息

print(psutil.net_if_stats()) # 获取网络接口状态

print(psutil.net_connections())

print(psutil.pids())

p = psutil.Process(3776)

print(p.name())

print(p.exe())

print(psutil.test())
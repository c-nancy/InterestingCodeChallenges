import time

# Question: given the local time and timestamp of user device, calculate the time zone of this device.

# Input:
# timestamp: the timestamp of user device when executed
# localtime: the local time provided by user device at the same time

# Output: the UTC time zone

# 1. Calculate the according time of UTC 0 with given timestamp.
# 2. Calculate the difference of hour between UTC 0 and local time.

# 给出设备时间戳和读取到的设备本地时间，计算设备所在的时区。
# 输入：设备时间戳，本地时间
# 输出：设备对应的UTC时区
# 思路：①使用时间戳计算零时区的对应时间，②计算零时区与设备时间的小时差


def local_time_to_timezone(timestamp, localtime):
    local_time = time.strptime(localtime, "%Y %m %d %H %M %S")
    hour_utc_0 = (timestamp % 86400) // 3600
    difference = local_time.tm_hour - hour_utc_0
    if difference > 0:
        difference = "+" + str(abs(difference))
    elif difference < 0:
        difference = "-" + str(abs(difference))
    return difference


print(local_time_to_timezone(1530522056, "2018 7 2 17 0 56"))
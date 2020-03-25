import time

cur_time = str(time.localtime(time.time()).tm_hour) + ":" + str(time.localtime(time.time()).tm_min)

print(cur_time)
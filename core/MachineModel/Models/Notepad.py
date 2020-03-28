import os
import psutil
import time


get_pid = int(os.getpid())

print(psutil.Process(pid=get_pid).num_threads())

# cur_time = str(time.localtime(time.time()).tm_hour) + ":" + str(time.localtime(time.time()).tm_min)

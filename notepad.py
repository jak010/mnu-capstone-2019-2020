from datetime import datetime

import time
print(time.localtime().tm_min ==13)


# for x in range(100000000):
#     cur_date = str(time.localtime(time.time()).tm_year) +"/"+str(time.localtime(time.time()).tm_mon)+"/"+str(time.localtime(time.time()).tm_mday)
#     cur_time = str(time.localtime(time.time()).tm_hour-12)+":"+str(time.localtime(time.time()).tm_min)+":"+str(time.localtime(time.time()).tm_sec)
#
#     print(cur_date+"/"+cur_time)

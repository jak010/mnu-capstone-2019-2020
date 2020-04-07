
import psutil
from pprint import pprint
import time

cur_date = str(time.localtime(time.time()).tm_year) + "-" + str(
    time.localtime(time.time()).tm_mon) + "-" + str(
    time.localtime(time.time()).tm_mday)
processList = []

for x in psutil.process_iter():
    if ("svchost.exe" in x.name() or "chrome.exe" in x.name()):
        pass
    elif "System Idle Process" in x.name():
        pass
    else:
        processList.append([x.name(),cur_date])

print(len(processList))

pprint(processList)
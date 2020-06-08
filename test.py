import psutil
from operator import itemgetter

processList = [ (x.info['name'],x.info['memory_percent']) for x in psutil.process_iter(attrs=['name', 'memory_percent'])]
filterList = []
for x in range(0,len(processList)):
    if "chrome.exe" in processList[x][0]: continue
    if "pycharm64.exe" in processList[x][0]: continue
    if "python.exe" in processList[x][0]: continue
    if "MemCompression" in processList[x][0]: continue
    if "System Idle Process" in processList[x][0]: continue

    filterList.append([processList[x][0],processList[x][1]])

test = sorted(filterList,key=itemgetter(1),reverse=True)

returnRank = [ x[0] for x in test[0:5]]
returnRank = ' '.join(returnRank)
print(returnRank)

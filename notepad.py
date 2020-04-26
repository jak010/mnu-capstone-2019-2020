import psutil

def warning_memory_singal():
    tempList = list()
    data_list = list()
    dataTopName = list()

    for x in psutil.process_iter(attrs=['name', 'username', 'memory_percent']):
        data_list.append([x.info['memory_percent'], x.info['name']])

    tempList = [[str(data_list[y][0]), data_list[y][1]] for y in range(0, len(data_list))]
    floatList = [[float(tempList[z][0]), tempList[z][1]] for z in range(0, len(tempList))]

    dataTop = sorted(floatList, reverse=True)

    for _ in range(0, 5):
        dataTopName.append(dataTop[_][1])

    returnStringValue = ", ".join(dataTopName)

    return returnStringValue

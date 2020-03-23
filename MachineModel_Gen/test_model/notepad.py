
import csv

x= list()
y=  list()

with open("../../csvDIR/Example03.csv","r") as read:
    for _ in read.readlines():
        if (len(_) < 21):
            tot_process,tot_threads = _.split(",")[1], _.split(",")[2]
            print(tot_process,tot_threads)
print(x)

xData = x # 프로세스 수
yData = y # 쓰레드 수

print(xData)
import csv

import matplotlib
import matplotlib.pyplot as plt


fig = plt.figure()
x_thread = list()
y_process =  list()
f = open("../csvDIR/Example01.csv","r")
rdr = csv.reader(f)
try:
    for line in rdr:
        tot_process, tot_thread = line[0].split(" ")[1],line[0].split(" ")[2]
        x_thread.append(tot_thread)
        y_process.append(tot_process)
except:
    pass
plt.scatter(x_thread,y_process ,label="Example01")
plt.xlabel("process")
plt.ylabel("thread")
plt.legend()
plt.show()

f.close()
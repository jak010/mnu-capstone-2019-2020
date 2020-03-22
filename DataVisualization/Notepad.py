import csv

import seaborn as sns
import matplotlib.pyplot as plt


x= list()
y=  list()
f = open("../csvDIR/Example01.csv","r")
rdr = csv.reader(f)
try:
    for line in rdr:
        tot_process, tot_thread = line[0].split(" ")[1],line[0].split(" ")[2]
        x.append(tot_process)
        y.append(tot_thread)
except:
    pass
sns.jointplot(x,y)
plt.show()
f.close()
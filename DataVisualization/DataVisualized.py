import collections
import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from collections import Counter
x = list()
y = list()
z = list()

fig = plt.figure()
#  =======================  process ===========================
ax1 = fig.add_subplot(2,2,1)

data = pd.read_csv("../csvDIR/Example03.csv")
data = pd.DataFrame(data)

k_data = []
y_data = []

for key,val in Counter(data["process"]).items():
    k_data.append(key)
    y_data.append(val)

k_data =sorted(k_data,reverse=True)
y_data = sorted(y_data,reverse=True)

ax1.plot(k_data,y_data)

#  =======================  thread ===========================
ax2 = fig.add_subplot(2,2,3)
data = pd.read_csv("../csvDIR/Example03.csv")
data = pd.DataFrame(data)

k_data = []
y_data = []

for key,val in Counter(data["threads"]).items():
    k_data.append(key)
    y_data.append(val)

k_data =sorted(k_data,reverse=True)
y_data = sorted(y_data,reverse=True)


ax2.scatter(k_data,y_data,marker="*",s=20,edgecolor="g")

#  =======================  process,thread ===========================
ax3 = fig.add_subplot(1,2,2)

data = pd.read_csv("../csvDIR/Example03.csv")
data = pd.DataFrame(data)

ax3.scatter(data["threads"],data["process"],color='1',marker="*",s=20,edgecolor="b")

plt.show()
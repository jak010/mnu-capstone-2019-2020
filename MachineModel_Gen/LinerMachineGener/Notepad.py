import pandas as pd

csv_text = pd.read_csv("../../csvDIR/Example03.csv",skiprows=[1,2])

xData = []
for x in csv_text.values.tolist():
    print(x)
    process, threads = x[1],x[2]
    xData.append([process,threads])

# print(len(xData))
yData = [0 for x in range(0,len(xData))]
print(yData)
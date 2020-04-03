# Data Visualized Source

import pandas as pd
import matplotlib.pyplot as plt

#  ======================= Process Visualized ===========================
def process_grpah():
    process_grpah = fig.add_subplot(2, 2, 1)
    process_grpah.set_title("process Usage")

    data = pd.read_csv(train_path)
    data = pd.DataFrame(data)

    process_grpah.scatter(data["memory_percent"],data["threads"] )

#  ======================= Memory Percent  Usage Visualized ===========================
def memory_usage():
    # x  : memory usage data
    # y  : process data
    memoryUsage = fig.add_subplot(2, 2, 2)
    memoryUsage.set_title("Memory Usage")

    data = pd.read_csv(train_path)
    data = pd.DataFrame(data)

    memoryUsage.scatter(data["memory_percent"],data["process"])

if __name__ == '__main__':
    train_path = "../csvDataSet/TrainSet.csv"
    fig = plt.figure()

    process_grpah()
    memory_usage()

    plt.subplots_adjust()
    plt.show()
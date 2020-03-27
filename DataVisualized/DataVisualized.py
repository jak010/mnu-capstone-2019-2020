# Data Visualized Source

import pandas as pd
import matplotlib.pyplot as plt

from collections import Counter

#  ======================= Process Visualized ===========================
def process_visualized():
    k_data = []
    y_data = []

    ax1 = fig.add_subplot(2, 2, 1)

    data = pd.read_csv(train_path)
    data = pd.DataFrame(data)

    for key, val in Counter(data["process"]).items():
        k_data.append(key)
        y_data.append(val)

    k_data = sorted(k_data, reverse=True)
    y_data = sorted(y_data, reverse=True)

    ax1.plot(k_data, y_data)


#  =======================  Thread Visualized ===========================
def thread_visualized():
    k_data = []
    y_data = []

    ax2 = fig.add_subplot(2, 2, 3)
    data = pd.read_csv(train_path)
    data = pd.DataFrame(data)

    for key, val in Counter(data["threads"]).items():
        k_data.append(key)
        y_data.append(val)

    k_data = sorted(k_data, reverse=True)
    y_data = sorted(y_data, reverse=True)

    ax2.scatter(k_data, y_data, marker="*", s=20, edgecolor="g")

#  =======================  process,thread ===========================
def process_thread_visualized():
    ax3 = fig.add_subplot(1, 2, 2)

    data = pd.read_csv(train_path)
    data = pd.DataFrame(data)

    ax3.scatter(data["threads"], data["process"], color='1', marker="*", s=20, edgecolor="b")


if __name__ == '__main__':
    train_path = "../csvDataSet/TrainSet.csv"
    fig = plt.figure()

    process_visualized()
    thread_visualized()
    process_thread_visualized()

    plt.show()
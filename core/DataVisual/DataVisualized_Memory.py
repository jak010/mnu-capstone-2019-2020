import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualized_time_0():
    returnList = []
    for _ in range(0,6):
        train_path = "./core/csvDataSet/TrainSet"+str(_)+".csv"
        df = pd.read_csv(train_path)
        df['time'] = df['time'].str.slice(start=0, stop=1)
        dataframe_visualized = df.groupby(by=['time'], as_index=False).mean()
        returnList.append([dataframe_visualized])
    return returnList


def visualized_time_1():
    returnList = []
    for _ in range(0,6):
        if _ == 0:
            train_path = "./core/csvDataSet/TrainSet" + str(_) + ".csv"
            # train_path = "../csvDataSet/TrainSet" + str(_) + ".csv"
            df = pd.read_csv(train_path)
            df['time'] = pd.to_numeric(df['time'].str.slice(start=0, stop=1))
            dataframe_visualized = df.groupby(by=['time'], as_index=False).mean()
            # print(dataframe_visualized)
            returnList.append([dataframe_visualized['time'].values.tolist(), dataframe_visualized['memory_usage'].values.tolist()])
        else:
            train_path = "./core/csvDataSet/TrainSet" + str(_) + ".csv"
            df = pd.read_csv(train_path)
            df['time'] = pd.to_numeric(df['time'].str.slice(start=0, stop=2))
            dataframe_visualized = df.groupby(by=['time'], as_index=False).mean()
            # print(dataframe_visualized)
            returnList.append([dataframe_visualized['time'].values.tolist(), dataframe_visualized['memory_usage'].values.tolist()])

    return returnList

# def visualized_time_1():
#     train_path = "C://Users//user//Desktop//Source//Castone//core//csvDataSet//TrainSet1.csv"
#
#     df = pd.read_csv(train_path)
#     df['time'] = df['time'].str.slice(start=0, stop=2)
#     dataframe_visualized = df.groupby(by=['time'], as_index=False).mean()
#
#     process_grpah = fig.add_subplot(3, 2, 2)
#     process_grpah.plot(dataframe_visualized['time'], dataframe_visualized['memory_usage'])
#
# def visualized_time_2():
#     train_path = "C://Users//user//Desktop//Source//Castone//core//csvDataSet//TrainSet2.csv"
#
#     df = pd.read_csv(train_path)
#     df['time'] = df['time'].str.slice(start=0, stop=2)
#     dataframe_visualized = df.groupby(by=['time'], as_index=False).mean()
#
#     process_grpah = fig.add_subplot(3, 2, 3)
#     process_grpah.plot(dataframe_visualized['time'], dataframe_visualized['memory_usage'])
#
# def visualized_time_3():
#     train_path = "C://Users//user//Desktop//Source//Castone//core//csvDataSet//TrainSet3.csv"
#
#     df = pd.read_csv(train_path)
#     df['time'] = df['time'].str.slice(start=0, stop=2)
#     dataframe_visualized = df.groupby(by=['time'], as_index=False).mean()
#
#     process_grpah = fig.add_subplot(3, 2, 4)
#     process_grpah.plot(dataframe_visualized['time'], dataframe_visualized['memory_usage'])
#
# def visualized_time_4():
#     train_path = "C://Users//user//Desktop//Source//Castone//core//csvDataSet//TrainSet4.csv"
#
#     df = pd.read_csv(train_path)
#     df['time'] = df['time'].str.slice(start=0, stop=2)
#     dataframe_visualized = df.groupby(by=['time'], as_index=False).mean()
#
#     process_grpah = fig.add_subplot(3, 2, 5)
#     process_grpah.plot(dataframe_visualized['time'], dataframe_visualized['memory_usage'])
#
# def visualized_time_5():
#     train_path = "C://Users//user//Desktop//Source//Castone//core//csvDataSet//TrainSet5.csv"
#
#     df = pd.read_csv(train_path)
#     df['time'] = df['time'].str.slice(start=0, stop=2)
#     dataframe_visualized = df.groupby(by=['time'], as_index=False).mean()
#
#     process_grpah = fig.add_subplot(3, 2, 6)
#     process_grpah.plot(dataframe_visualized['time'], dataframe_visualized['memory_usage'])

if __name__ == '__main__':
    # r = visualized_time_1()

    train_path = "../csvDataSet/TrainSet0.csv"
    df = pd.read_csv(train_path)
    df['time'] = df['time'].str.slice(start=0, stop=1)
    dataframe_visualized = df.groupby(by=['time'], as_index=False).mean()
    retlist = [[dataframe_visualized['time'].values.tolist(),dataframe_visualized['memory_usage'].values.tolist()]]
    print(retlist)
    print(retlist[0][0])
    print(retlist[0][1])



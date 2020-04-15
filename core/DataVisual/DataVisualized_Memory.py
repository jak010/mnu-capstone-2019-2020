import pandas as pd

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


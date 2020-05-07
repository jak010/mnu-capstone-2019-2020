
# 2020 03 22
# Feature : 데이터가 수집된 일시 ,총 프로세스 ,총 쓰레드 갯수

import os
import csv
import psutil
import pandas as pd

from time import localtime

class dataLibrary:
    def __init__(self):
        pass

    def dataCollecting(self,exit_flag):
        cur_time = str(localtime().tm_min) + ":" + str(localtime().tm_sec)
        # 0~10분 까지
        if len(cur_time.split(":")[0]) == 1:
            print("0분대")
            train_path = "./core/csvDataSet/TrainSet0.csv"
            if os.path.isfile(train_path):
                try:
                    f = open(train_path, "a+", newline='')
                    wr = csv.writer(f)

                    # 총 프로세스 , 총 쓰레드 갯수
                    tot_process_number = len([x for x in psutil.pids()])
                    tot_thread_number = sum([x.num_threads() for x in psutil.process_iter()])
                    memory_usage = psutil.virtual_memory()
                    print(cur_time, tot_process_number, tot_thread_number, memory_usage.percent)

                    wr.writerow([cur_time, tot_process_number, tot_thread_number, memory_usage.percent])
                    f.close()
                except Exception as e:
                    print(e)
            else:
                f = open(train_path, "a+", newline='')
                wr = csv.writer(f)
                wr.writerow(["time", "process", "threads", "memory_usage"])
                f.close()

        elif len(cur_time.split(":")[0]) == 2:
            if int(cur_time.split(":")[0][0]) == 1:
                print("10분대")
                train_path = "./core/csvDataSet/TrainSet1.csv"
                if os.path.isfile(train_path):
                    try:
                        f = open(train_path, "a+", newline='')
                        wr = csv.writer(f)

                        # 총 프로세스 , 총 쓰레드 갯수
                        tot_process_number = len([x for x in psutil.pids()])
                        tot_thread_number = sum([x.num_threads() for x in psutil.process_iter()])
                        memory_usage = psutil.virtual_memory()
                        print(cur_time, tot_process_number, tot_thread_number, memory_usage.percent)

                        wr.writerow([cur_time, tot_process_number, tot_thread_number, memory_usage.percent])
                        f.close()
                    except Exception as e:
                        print(e)
                else:
                    f = open(train_path, "a+", newline='')
                    wr = csv.writer(f)
                    wr.writerow(["time", "process", "threads", "memory_usage"])
                    f.close()


            elif int(cur_time.split(":")[0][0]) == 2:
                print("20분대")
                train_path = "./core/csvDataSet/TrainSet2.csv"
                if os.path.isfile(train_path):
                    try:
                        f = open(train_path, "a+", newline='')
                        wr = csv.writer(f)

                        # 총 프로세스 , 총 쓰레드 갯수
                        tot_process_number = len([x for x in psutil.pids()])
                        tot_thread_number = sum([x.num_threads() for x in psutil.process_iter()])
                        memory_usage = psutil.virtual_memory()
                        print(cur_time, tot_process_number, tot_thread_number, memory_usage.percent)

                        wr.writerow([cur_time, tot_process_number, tot_thread_number, memory_usage.percent])
                        f.close()
                    except Exception as e:
                        print(e)
                else:
                    f = open(train_path, "a+", newline='')
                    wr = csv.writer(f)
                    wr.writerow(["time", "process", "threads", "memory_usage"])
                    f.close()

            elif int(cur_time.split(":")[0][0]) == 3:
                print("30분대")
                train_path = "./core/csvDataSet/TrainSet3.csv"
                if os.path.isfile(train_path):
                    try:
                        f = open(train_path, "a+", newline='')
                        wr = csv.writer(f)

                        # 총 프로세스 , 총 쓰레드 갯수
                        tot_process_number = len([x for x in psutil.pids()])
                        tot_thread_number = sum([x.num_threads() for x in psutil.process_iter()])
                        memory_usage = psutil.virtual_memory()
                        print(cur_time, tot_process_number, tot_thread_number, memory_usage.percent)

                        wr.writerow([cur_time, tot_process_number, tot_thread_number, memory_usage.percent])
                        f.close()
                    except Exception as e:
                        print(e)
                else:
                    f = open(train_path, "a+", newline='')
                    wr = csv.writer(f)
                    wr.writerow(["time", "process", "threads", "memory_usage"])
                    f.close()

            elif int(cur_time.split(":")[0][0]) == 4:
                print("40분대")
                train_path = "./core/csvDataSet/TrainSet4.csv"
                if os.path.isfile(train_path):
                    try:
                        f = open(train_path, "a+", newline='')
                        wr = csv.writer(f)

                        # 총 프로세스 , 총 쓰레드 갯수
                        tot_process_number = len([x for x in psutil.pids()])
                        tot_thread_number = sum([x.num_threads() for x in psutil.process_iter()])
                        memory_usage = psutil.virtual_memory()
                        print(cur_time, tot_process_number, tot_thread_number, memory_usage.percent)

                        wr.writerow([cur_time, tot_process_number, tot_thread_number, memory_usage.percent])
                        f.close()
                    except Exception as e:
                        print(e)
                else:
                    f = open(train_path, "a+", newline='')
                    wr = csv.writer(f)
                    wr.writerow(["time", "process", "threads", "memory_usage"])
                    f.close()

            elif int(cur_time.split(":")[0][0]) == 5:
                print("50분대")
                train_path = "./core/csvDataSet/TrainSet5.csv"
                if os.path.isfile(train_path):
                    try:
                        f = open(train_path, "a+", newline='')
                        wr = csv.writer(f)

                        # 총 프로세스 , 총 쓰레드 갯수
                        tot_process_number = len([x for x in psutil.pids()])
                        tot_thread_number = sum([x.num_threads() for x in psutil.process_iter()])
                        memory_usage = psutil.virtual_memory()
                        print(cur_time, tot_process_number, tot_thread_number, memory_usage.percent)

                        wr.writerow([cur_time, tot_process_number, tot_thread_number, memory_usage.percent])
                        f.close()
                    except Exception as e:
                        print(e)
                else:
                    f = open(train_path, "a+", newline='')
                    wr = csv.writer(f)
                    wr.writerow(["time", "process", "threads", "memory_usage"])
                    f.close()

    def warning_memory_singal(self):
        data_list = list()
        dataTopName = list()

        remove_list = ["pycharm64.exe", "python.exe", "MemCompression", "chrome.exe"]

        for x in psutil.process_iter(attrs=['name', 'username', 'memory_percent']):
            if (x.info['name'] in "pycharm64.exe") or (x.info['name'] in "python.exe"):
                # first remove
                pass
            elif (x.info["name"] in "MemCompression") or (x.info['name'] in "chrome.exe"):
                # second remove
                pass
            else:
                data_list.append([x.info['memory_percent'], x.info['name']])

        tempList = [[str(data_list[y][0]), data_list[y][1]] for y in range(0, len(data_list))]
        floatList = [[float(tempList[z][0]), tempList[z][1]] for z in range(0, len(tempList))]

        dataTop = sorted(floatList, reverse=True)

        for _ in range(0, 5):
            dataTopName.append(dataTop[_][1])

        returnStringValue = ", ".join(dataTopName)

        return returnStringValue

    def visualized_train_data(self):
        """
            이 함수는 core/csvDatset/ 경로의 train 데이터를 시각화 하는 데 사용 됩니다.

            Args:
                None

            Return:
                return data : list
        """
        returnList = []
        for _ in range(0, 6):
            if _ == 0:
                train_path = "./core/csvDataSet/TrainSet" + str(_) + ".csv"
                df = pd.read_csv(train_path)
                df['time'] = pd.to_numeric(df['time'].str.slice(start=0, stop=1))
                dataframe_visualized = df.groupby(by=['time'], as_index=False).mean()
                returnList.append([dataframe_visualized['time'].values.tolist(),
                                   dataframe_visualized['memory_usage'].values.tolist()])

            else:
                train_path = "./core/csvDataSet/TrainSet" + str(_) + ".csv"
                df = pd.read_csv(train_path)
                df['time'] = pd.to_numeric(df['time'].str.slice(start=0, stop=2))
                dataframe_visualized = df.groupby(by=['time'], as_index=False).mean()
                returnList.append([dataframe_visualized['time'].values.tolist(),
                                   dataframe_visualized['memory_usage'].values.tolist()])

        return returnList








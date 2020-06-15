# 2020 03 22
# Feature : 데이터가 수집된 일시 ,총 프로세스 ,총 쓰레드 갯수
from time import localtime

import os
import csv
import psutil
import pandas as pd
from operator import itemgetter

class DataParsing:
    def __init__(self):
        pass

    @classmethod
    def datacollectingChk(cls,req):
        cur_time = str(localtime().tm_min) + ":" + str(localtime().tm_sec)

        train_path = str()
        if len(cur_time.split(":")[0]) == 1:
            train_path = "0"
        elif len(cur_time.split(":")[0]) == 2:
            if int(cur_time.split(":")[0][0]) == 1:
                train_path = "1"
            elif int(cur_time.split(":")[0][0]) == 2:
                train_path = "2"
            elif int(cur_time.split(":")[0][0]) == 3:
                train_path = "3"
            elif int(cur_time.split(":")[0][0]) == 4:
                train_path = "4"
            elif int(cur_time.split(":")[0][0]) == 5:
                train_path = "5"

        return  train_path

    @classmethod
    def data_collecting(cls,req_flag):
        cur_time = str(localtime().tm_min) + ":" + str(localtime().tm_sec)
        # 0~10분 까지
        if len(cur_time.split(":")[0]) == 1:
            print("0분대")
            train_path = "./core/csvDataSet/TrainSet0.csv"
            if os.path.isfile(train_path):
                try:
                    file_open_obj = open(train_path, "a+", newline='')
                    write_row = csv.writer(file_open_obj)

                    # 총 프로세스 , 총 쓰레드 갯수
                    tot_process_number = len(list(_ for _ in psutil.pids()))
                    tot_thread_number = sum([_.num_threads() for _ in psutil.process_iter()])
                    memory_usage = psutil.virtual_memory()
                    print(cur_time, tot_process_number, tot_thread_number, memory_usage.percent)

                    write_row.writerow(
                        [
                            cur_time, tot_process_number,
                            tot_thread_number, memory_usage.percent
                        ]
                    )
                    file_open_obj.close()
                except (FileNotFoundError) as err_msg:
                    print(err_msg)
            else:
                file_open_obj = open(train_path, "a+", newline='')
                write_row = csv.writer(file_open_obj)
                write_row.writerow(["time", "process", "threads", "memory_usage"])
                file_open_obj.close()

        elif len(cur_time.split(":")[0]) == 2:
            if int(cur_time.split(":")[0][0]) == 1:
                print("10분대")
                train_path = "./core/csvDataSet/TrainSet1.csv"
                if os.path.isfile(train_path):
                    try:
                        file_open_obj = open(train_path, "a+", newline='')
                        write_row = csv.writer(file_open_obj)

                        # 총 프로세스 , 총 쓰레드 갯수
                        tot_process_number = len(list(_ for _ in psutil.pids()))
                        tot_thread_number = sum([x.num_threads() for x in psutil.process_iter()])
                        memory_usage = psutil.virtual_memory()

                        print(cur_time, tot_process_number,
                              tot_thread_number, memory_usage.percent)

                        write_row.writerow([cur_time, tot_process_number,
                                            tot_thread_number, memory_usage.percent])
                        file_open_obj.close()
                    except (FileNotFoundError) as err_msg:
                        print(err_msg)
                else:
                    file_open_obj = open(train_path, "a+", newline='')
                    write_row = csv.writer(file_open_obj)
                    write_row.writerow(["time", "process", "threads", "memory_usage"])
                    file_open_obj.close()


            elif int(cur_time.split(":")[0][0]) == 2:
                print("20분대")
                train_path = "./core/csvDataSet/TrainSet2.csv"
                if os.path.isfile(train_path):
                    try:
                        file_open_obj = open(train_path, "a+", newline='')
                        write_row = csv.writer(file_open_obj)

                        # 총 프로세스 , 총 쓰레드 갯수
                        tot_process_number = len(list(_ for _ in psutil.pids()))
                        tot_thread_number = sum([x.num_threads() for x in psutil.process_iter()])
                        memory_usage = psutil.virtual_memory()
                        print(cur_time, tot_process_number, tot_thread_number, memory_usage.percent)

                        write_row.writerow([cur_time, tot_process_number,
                                            tot_thread_number, memory_usage.percent])
                        file_open_obj.close()
                    except (FileNotFoundError) as err_msg:
                        print(err_msg)
                else:
                    file_open_obj = open(train_path, "a+", newline='')
                    write_row = csv.writer(file_open_obj)
                    write_row.writerow(["time", "process", "threads", "memory_usage"])
                    file_open_obj.close()

            elif int(cur_time.split(":")[0][0]) == 3:
                print("30분대")
                train_path = "./core/csvDataSet/TrainSet3.csv"
                if os.path.isfile(train_path):
                    try:
                        file_open_obj = open(train_path, "a+", newline='')
                        write_row = csv.writer(file_open_obj)

                        # 총 프로세스 , 총 쓰레드 갯수
                        tot_process_number = len(list(_ for _ in psutil.pids()))
                        tot_thread_number = sum([x.num_threads() for x in psutil.process_iter()])
                        memory_usage = psutil.virtual_memory()
                        print(cur_time, tot_process_number, tot_thread_number, memory_usage.percent)

                        write_row.writerow([cur_time, tot_process_number,
                                            tot_thread_number, memory_usage.percent])
                        file_open_obj.close()
                    except (FileNotFoundError) as err_msg:
                        print(err_msg)
                else:
                    file_open_obj = open(train_path, "a+", newline='')
                    write_row = csv.writer(file_open_obj)
                    write_row.writerow(["time", "process", "threads", "memory_usage"])
                    file_open_obj.close()

            elif int(cur_time.split(":")[0][0]) == 4:
                print("40분대")
                train_path = "./core/csvDataSet/TrainSet4.csv"
                if os.path.isfile(train_path):
                    try:
                        file_open_obj = open(train_path, "a+", newline='')
                        write_row = csv.writer(file_open_obj)

                        # 총 프로세스 , 총 쓰레드 갯수
                        tot_process_number = len(list(_ for _ in psutil.pids()))
                        tot_thread_number = sum([x.num_threads() for x in psutil.process_iter()])
                        memory_usage = psutil.virtual_memory()
                        print(cur_time, tot_process_number, tot_thread_number, memory_usage.percent)

                        write_row.writerow([cur_time, tot_process_number,
                                            tot_thread_number, memory_usage.percent])
                        file_open_obj.close()
                    except (FileNotFoundError) as err_msg:
                        print(err_msg)
                else:
                    file_open_obj = open(train_path, "a+", newline='')
                    write_row = csv.writer(file_open_obj)
                    write_row.writerow(["time", "process", "threads", "memory_usage"])
                    file_open_obj.close()

            elif int(cur_time.split(":")[0][0]) == 5:
                print("50분대")
                train_path = "./core/csvDataSet/TrainSet5.csv"
                if os.path.isfile(train_path):
                    try:
                        file_open_obj = open(train_path, "a+", newline='')
                        write_row = csv.writer(file_open_obj)

                        # 총 프로세스 , 총 쓰레드 갯수
                        tot_process_number = len(list(_ for _ in psutil.pids()))
                        tot_thread_number = sum([x.num_threads() for x in psutil.process_iter()])
                        memory_usage = psutil.virtual_memory()
                        print(cur_time, tot_process_number, tot_thread_number, memory_usage.percent)

                        write_row.writerow([cur_time, tot_process_number,
                                            tot_thread_number, memory_usage.percent])
                        file_open_obj.close()
                    except (FileNotFoundError) as err_msg:
                        print(err_msg)
                else:
                    file_open_obj = open(train_path, "a+", newline='')
                    write_row = csv.writer(file_open_obj)
                    write_row.writerow(["time", "process", "threads", "memory_usage"])
                    file_open_obj.close()

    @classmethod
    def warning_memory_singal(cls):
        processList = [(x.info['name'], x.info['memory_percent']) for x in
                       psutil.process_iter(attrs=['name', 'memory_percent'])]
        filterList = []
        for x in range(0, len(processList)):
            if "chrome.exe" in processList[x][0]: continue
            if "pycharm64.exe" in processList[x][0]: continue
            if "python.exe" in processList[x][0]: continue
            if "MemCompression" in processList[x][0]: continue
            if "System Idle Process" in processList[x][0]: continue

            filterList.append([processList[x][0], processList[x][1]])

        test = sorted(filterList, key=itemgetter(1), reverse=True)

        returnRank = [x[0] for x in test[0:5]]
        returnRank = ' '.join(returnRank)

        return returnRank

    @classmethod
    def visualized_train_data(cls):
        """
            이 함수는 core/csvDatset/ 경로의 train 데이터를 시각화 하는 데 사용 됩니다.

            Args:
                None

            Return:
                return data : list
        """
        return_list = []
        for _ in range(0, 6):
            if _ == 0:
                train_path = "./core/csvDataSet/TrainSet" + str(_) + ".csv"
                data_frame = pd.read_csv(train_path)
                data_frame['time'] = pd.to_numeric(data_frame['time'].str.slice(start=0, stop=1))
                data_frame_visualized = data_frame.groupby(by=['time'], as_index=False).mean()
                return_list.append([data_frame_visualized['time'].values.tolist(),
                                    data_frame_visualized['memory_usage'].values.tolist()])

            else:

                train_path = "./core/csvDataSet/TrainSet" + str(_) + ".csv"
                data_frame = pd.read_csv(train_path)

                data_frame['time'] = pd.to_numeric(data_frame['time'].str.slice(start=0, stop=2))
                data_frame_visualized = data_frame.groupby(by=['time'], as_index=False).mean()
                return_list.append([data_frame_visualized['time'].values.tolist(),
                                    data_frame_visualized['memory_usage'].values.tolist()])

        return return_list

    @classmethod
    def visualized_train_data_statical(cls):
        """
            이 함수는 core/csvDatset/ 경로의 train 데이터의 통계를 내는데 사용합니다.
            Return:
                return data : list
        """
        return_list = []
        avg_list = []

        for _ in range(0, 6):
            if _ == 0:
                train_path = "./core/csvDataSet/TrainSet" + str(_) + ".csv"
                data_frame = pd.read_csv(train_path)
                data_frame['time'] = pd.to_numeric(data_frame['time'].str.slice(start=0, stop=1))
                data_frame_visualized = data_frame.groupby(by=['time'], as_index=False).mean()
                return_list.append([data_frame_visualized['time'].values.tolist(),
                                    data_frame_visualized['memory_usage'].values.tolist()])

            else:
                train_path = "./core/csvDataSet/TrainSet" + str(_) + ".csv"
                data_frame = pd.read_csv(train_path)
                data_frame['time'] = pd.to_numeric(data_frame['time'].str.slice(start=0, stop=2))
                data_frame_visualized = data_frame.groupby(by=['time'], as_index=False).mean()
                return_list.append([data_frame_visualized['time'].values.tolist(),
                                    data_frame_visualized['memory_usage'].values.tolist()])

        for _ in range(0, 6):
            with open("./core/csvDataSet/TrainSet" + str(_) + ".csv", "r") as f:
                fd = csv.reader(f)
                row_cnt = len([row for row in fd])
                avg_list.append([sum(return_list[_][1]) / 10, row_cnt])

        return avg_list

# 2020 03 22
# Feature : 데이터가 수집된 일시 ,총 프로세스 ,총 쓰레드 갯수
from time import localtime

import os
import csv
import psutil
import pandas as pd

class DataParsing:
    def __init__(self):
        pass

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
        data_list = list()
        data_top_name = list()

        for process_ in psutil.process_iter(attrs=['name', 'username', 'memory_percent']):
            # first remove
            if (process_.info['name'] in "pycharm64.exe") \
                    or \
                    (process_.info['name'] in "python.exe"):
                pass

            # second remove
            elif (process_.info["name"] in "MemCompression") \
                    or \
                    (process_.info['name'] in "chrome.exe"):
                pass

            else:
                data_list.append([process_.info['memory_percent'], process_.info['name']])

        temp_list = [[str(data_list[y][0]), data_list[y][1]] for y in range(0, len(data_list))]
        float_list = [[float(temp_list[z][0]), temp_list[z][1]] for z in range(0, len(temp_list))]

        data_top = sorted(float_list, reverse=True)

        for _ in range(0, 5):
            data_top_name.append(data_top[_][1])

        return_string_value = ", ".join(data_top_name)

        return return_string_value

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

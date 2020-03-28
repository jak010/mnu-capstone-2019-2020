# 2020 03 22
# Feature : 데이터가 수집된 일시 ,총 프로세스 ,총 쓰레드 갯수

import os
import csv
import time
import psutil

train_path = "../csvDataSet/TrainSet.csv"

# 파일이 있는 경우 헤더
if os.path.isfile(train_path):
    print(" ============= [+] File Exist On Path ==================" )

    while True:
        try:
            f = open(train_path, "a+", newline='')
            wr = csv.writer(f)

            cur_date = str(time.localtime(time.time()).tm_year) + "-" + str(
                time.localtime(time.time()).tm_mon) + "-" + str(
                time.localtime(time.time()).tm_mday)
            cur_time = str(time.localtime(time.time()).tm_hour - 12) + ":" + str(
                time.localtime(time.time()).tm_min)

            # 총 프로세스 , 총 쓰레드 갯수
            tot_process_number, tot_thread_number = len([x for x in psutil.pids()]), sum(
                [x.num_threads() for x in psutil.process_iter()])
            print(cur_date, tot_process_number, tot_thread_number)

            wr.writerow([cur_date, tot_process_number, tot_thread_number])

            f.close()
        except Exception as e:
            cur_date = str(time.localtime(time.time()).tm_year) + "-" + str(
                time.localtime(time.time()).tm_mon) + "-" + str(
                time.localtime(time.time()).tm_mday)
            cur_time = str(time.localtime(time.time()).tm_hour - 12) + ":" + str(
                time.localtime(time.time()).tm_min)

            print(cur_date, cur_time)
            continue

# 파일이 없는 경우 헤더
else :
    print(" ============= [+] File Not Exist On Path ==================")
    f = open("../csvDataSet/TrainSet.csv", "a+", newline='')
    wr = csv.writer(f)

    wr.writerow(["time", "process", "threads"])
    while True:
        try:
            f = open(train_path, "a+", newline='')
            wr = csv.writer(f)

            cur_date = str(time.localtime(time.time()).tm_year) + "-" + str(
                time.localtime(time.time()).tm_mon) + "-" + str(
                time.localtime(time.time()).tm_mday)
            cur_time = str(time.localtime(time.time()).tm_hour - 12) + ":" + str(
                time.localtime(time.time()).tm_min)

            # 총 프로세스 , 총 쓰레드 갯수
            tot_process_number, tot_thread_number = len([x for x in psutil.pids()]), sum(
                [x.num_threads() for x in psutil.process_iter()])
            print(cur_date, tot_process_number, tot_thread_number)

            wr.writerow([cur_date, tot_process_number, tot_thread_number])

            f.close()
        except Exception as e:
            cur_date = str(time.localtime(time.time()).tm_year) + "-" + str(
                time.localtime(time.time()).tm_mon) + "-" + str(
                time.localtime(time.time()).tm_mday)
            cur_time = str(time.localtime(time.time()).tm_hour - 12) + ":" + str(
                time.localtime(time.time()).tm_min)

            print(cur_date, cur_time)
            continue
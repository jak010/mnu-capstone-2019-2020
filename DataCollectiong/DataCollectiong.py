# 2020 03 22
# Feature : 총 프로세스, 총 쓰레드 갯수
# cur_time : 데이터가 수집된 일시
import time
import csv
import psutil

f = open("../csvDIR/Example03.csv", "a+", newline='')
wr = csv.writer(f)

wr.writerow(["time","process","threads"])
while True:
    try:
        f = open("../csvDIR/Example03.csv", "a+", newline='')
        wr = csv.writer(f)

        cur_date = str(time.localtime(time.time()).tm_year) + "-" + str(time.localtime(time.time()).tm_mon) + "-" + str(
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
        cur_date = str(time.localtime(time.time()).tm_year) + "-" + str(time.localtime(time.time()).tm_mon) + "-" + str(
            time.localtime(time.time()).tm_mday)
        cur_time = str(time.localtime(time.time()).tm_hour - 12) + ":" + str(
            time.localtime(time.time()).tm_min)

        print(cur_date,cur_time)
        continue
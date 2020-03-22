
import time
import psutil

while True:
    if(time.localtime().tm_min == 45):
        break

    cur_date = str(time.localtime(time.time()).tm_year) + "/" + str(time.localtime(time.time()).tm_mon) + "/" + str(
        time.localtime(time.time()).tm_mday)
    cur_time = str(time.localtime(time.time()).tm_hour - 12) + ":" + str(
        time.localtime(time.time()).tm_min) + ":" + str(time.localtime(time.time()).tm_sec)


    # 총 프로세스 , 총 쓰레드 갯수
    tot_process_number, tot_thread_number = len([x for x in psutil.pids()]), sum(
        [x.num_threads() for x in psutil.process_iter()])
    print(cur_time ,tot_process_number, tot_thread_number)


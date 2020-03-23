import psutil


all_process = [ x.pid for x in psutil.process_iter() ]

# process number
print(all_process)
print(len(all_process))

#thread number
cnt =0
for x in range(0,len(all_process)): cnt += psutil.Process(pid=all_process[x]).num_threads()
print(cnt)


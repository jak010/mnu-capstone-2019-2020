import psutil


all_process = [x.pid for x in psutil.process_iter()]
thread_count = 0
for x in range(0, len(all_process)): thread_count += psutil.Process(pid=all_process[x]).num_threads()
data = [thread_count]

print(all_process, data)
# process

X1 = [len(all_process)]
# threads
X2 = data

cpu_mem = psutil.cpu_percent()

print(type(cpu_mem))

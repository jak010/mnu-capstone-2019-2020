
total_process = []
total_threads =[]
cpu_usage = []

with open("../../csvDataSet/TrainSet.csv","r") as read:
    for _ in read.readlines():
        if (len(_) < 34):
            tot_process,tot_threads,memory_percentage = _.split(",")[1], _.split(",")[2], _.split(",")[3].replace("\n","")
            print(tot_process)
            print(tot_threads)
            print(memory_percentage)

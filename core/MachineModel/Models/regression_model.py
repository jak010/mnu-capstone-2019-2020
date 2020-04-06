import os

# tensorflow warning message removed !
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import psutil
import tensorflow as tf

total_process = []
total_threads =[]
cpu_usage = []

with open("../../csvDataSet/TrainSet.csv","r") as read:
    for _ in read.readlines():
        if (len(_) < 34):
            tot_process,tot_threads,memory_percentage = _.split(",")[1], _.split(",")[2], _.split(",")[3].replace("\n","")
            total_process.append(tot_process)
            total_threads.append(tot_threads)
            cpu_usage.append(float(memory_percentage))

xData = total_process
yData = total_threads
zData = cpu_usage

print(xData)
print(yData)
print(zData)

# process
X1 = tf.compat.v1.placeholder(tf.float32,shape=[None])
# threads
X2 = tf.compat.v1.placeholder(tf.float32,shape=[None])

# mem_percent
Y = tf.compat.v1.placeholder(tf.float32,shape=[None])

#가중치
W1 = tf.Variable(tf.random_normal([1],seed=1))
W2 = tf.Variable(tf.random_normal([1],seed=1))

# 절편3
b = tf.Variable(tf.random_normal([1],seed=1))

# 가설식
H = X1 * W1 + X2*W2 +b

cost = tf.reduce_mean(tf.square(H-Y))

optimizer =  tf.compat.v1.train.GradientDescentOptimizer(learning_rate=0.00000001)

train = optimizer.minimize(cost)
init = tf.compat.v1.global_variables_initializer()
sess = tf.compat.v1.Session()
sess.run(init)


for step in range(8001):
    cost_,w1_,w2_,b_,_ = sess.run([cost,W1,W2,b,train] ,feed_dict={X1:xData,X2:yData,Y:zData})

    if step % 500 == 0:  # 500개 마다 모니터링
        print(cost_,w1_,w2_)

try:
    all_process = [x.pid for x in psutil.process_iter()]
    thread_count = 0
    for x in range(0, len(all_process)): thread_count += psutil.Process(pid=all_process[x]).num_threads()
    data = [thread_count]

    #process
    X1_process = len(all_process)

    # cpu_percent
    X2_threads_usage = data
    print(X1_process,X2_threads_usage)

    # memory usage
    predict = psutil.virtual_memory()

    print("Current Memory Percent : " ,predict.percent)
    print("Predict :", sess.run(H, feed_dict={X1: [X1_process], X2: X2_threads_usage}))
except Exception as e:
    print(e)

saver = tf.compat.v1.train.Saver()
saver_path = saver.save(sess,"./saved.cpkt")

print("학습된 모델을 저장했습니다.")

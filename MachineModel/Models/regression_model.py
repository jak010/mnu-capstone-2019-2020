import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import numpy as np
import tensorflow as tf

total_process = []
total_threads =[]

with open("../../csvDataSet/TrainSet.csv","r") as read:
    for _ in read.readlines():
        if (len(_) < 21):
            tot_process,tot_threads = _.split(",")[1], _.split(",")[2]
            total_process.append(tot_process)
            total_threads.append(tot_threads)

xData = total_threads
yData = total_process
#가중치
W = tf.Variable(tf.random_uniform([1],seed=1))
# 절편3
b = tf.Variable(tf.random_uniform([1],seed=1))

X = tf.compat.v1.placeholder(tf.float32)
Y = tf.compat.v1.placeholder(tf.float32)

# 가설식
H = (W + 0.025*X) + b
cost = tf.reduce_mean(tf.square(H-Y))

optimizer =  tf.compat.v1.train.GradientDescentOptimizer(learning_rate=0.004)

train = optimizer.minimize(cost)
init = tf.compat.v1.global_variables_initializer()
sess = tf.compat.v1.Session()
sess.run(init)

for i in range(1001):
    sess.run(train, feed_dict={X: xData, Y: yData})
    if i % 250 == 0:  # 500개 마다 모니터링
        print(i, sess.run(cost, feed_dict={X: xData, Y: yData}), sess.run(W), sess.run(b))

import psutil

try:
    all_process = [x.pid for x in psutil.process_iter()]
    thread_count = 0
    for x in range(0, len(all_process)): thread_count += psutil.Process(pid=all_process[x]).num_threads()

    data = [thread_count]

    # 프로세스의 수가 256일 때 예측되는 쓰레드의 수
    print(len(all_process),'[ Predict :',np.round(sess.run(H, feed_dict={X: data})[0]),']')
except:
    pass


saver = tf.compat.v1.train.Saver()
saver_path = saver.save(sess,"./saved.cpkt")

print("학습된 모델을 저장했습니다.")
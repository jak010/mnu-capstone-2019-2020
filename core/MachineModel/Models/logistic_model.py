import os

# tensorflow warning message removed !
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import psutil
import numpy as np
import tensorflow as tf

# threads,process
tot_infomic = []
none_data =[]

with open("../../csvDataSet/TrainSet.csv","r") as read:
    for _ in read.readlines():
        if (len(_) < 21):
            tot_process,tot_threads = _.split(",")[1], _.split(",")[2]
            tot_infomic.append([int(tot_threads),int(tot_process)])
            none_data.append([0])

xData = tot_infomic
yData = none_data

print(xData)
print(yData)

X = tf.compat.v1.placeholder(tf.float32,shape=[None,2])
Y = tf.compat.v1.placeholder(tf.float32,shape=[None,1])

#가중치
W = tf.Variable(tf.random_normal([2,1]),name="wight")
# 절편3
b = tf.Variable(tf.random_normal([1]),name="bias")
# 가설식

H =  tf.matmul(X,W)+b
cost = -tf.reduce_mean( Y * tf.log(H) + (1-Y)*(tf.log(1-H)))

train =  tf.compat.v1.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)

init = tf.compat.v1.global_variables_initializer()
sess = tf.compat.v1.Session()

predicted = tf.cast(H > 0.5, dtype=tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted,Y),dtype=tf.float32))

for step in range(3001):
    sess.run(init)
    if step % 250 == 0:  # 500개 마다 모니터링
        cost_val, _ = sess.run([cost, train], feed_dict={X: xData, Y: yData})
        # print(i, sess.run(cost, feed_dict={X: xData, Y: yData}), sess.run(W), sess.run(b))
        print(step , '\t',cost_val)

h,c,a = sess.run([H,predicted,accuracy],
                 feed_dict={X:xData,Y:yData}
                 )
print("\nHypothesis: ",h ,
      "\nCorrect (Y): ",c ,
      "\n Accuracy  :" ,a
      )

# try:
#     all_process = [x.pid for x in psutil.process_iter()]
#     thread_count = 0
#     for x in range(0, len(all_process)): thread_count += psutil.Process(pid=all_process[x]).num_threads()
#
#     data = [thread_count]
#
#     # 프로세스 대비 예측되는 쓰레드의 수
#     print(len(all_process),'[ Predict :',np.round(sess.run(H, feed_dict={X: data})[0]),']')
# except:
#     pass

saver = tf.compat.v1.train.Saver()
saver_path = saver.save(sess,"./saved.cpkt")

print("학습된 모델을 저장했습니다.")
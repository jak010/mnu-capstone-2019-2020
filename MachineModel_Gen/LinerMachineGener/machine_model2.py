import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


import tensorflow as tf
import pandas as pd
total_process = []
total_threads =[]

csv_text = pd.read_csv("../../csvDIR/Example03.csv",skiprows=[1,2])

xData = []

for x in csv_text.values.tolist():
    process, threads = x[1],x[2]
    xData.append([process,threads])

yData = [[1] for x in range(0,len(xData))]
#가중치
W = tf.Variable(tf.random_normal([2,1]),"weight")
# 절편
b = tf.Variable(tf.random_normal([1]),"bias")

X = tf.compat.v1.placeholder(tf.float32, shape=[None,2])
Y = tf.compat.v1.placeholder(tf.float32, shape=[None,1])

# 가설식
H = -tf.matmul(X,W) + b

cost = tf.reduce_mean(Y * tf.math.log(H) + (1-Y) * tf.math.log(1 - H))

optimizer =  tf.compat.v1.train.GradientDescentOptimizer(learning_rate=1e-2)

train = optimizer.minimize(cost)
init = tf.compat.v1.global_variables_initializer()
sess = tf.compat.v1.Session()
sess.run(init)

for i in range(1001):
    sess.run(train, feed_dict={X: xData, Y: yData})
    if i % 500 == 0:  # 500개 마다 모니터링
        print(i, sess.run(cost, feed_dict={X: xData, Y: yData}), sess.run(W), sess.run(b))

print(sess.run(H, feed_dict={X: [[240,3237]]}))  # 프로세스의 수가 256일 때 예측되는 쓰레드의 수

saver = tf.compat.v1.train.Saver()
saver_path = saver.save(sess,"./saved.cpkt")

print("학습된 모델을 저장했습니다.")
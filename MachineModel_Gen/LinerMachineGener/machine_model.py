import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


import tensorflow as tf

total_process = []
total_threads =[]

with open("../../csvDIR/Example03.csv","r") as read:
    for _ in read.readlines():
        if (len(_) < 21):
            tot_process,tot_threads = _.split(",")[1], _.split(",")[2]
            total_process.append(tot_process)
            total_threads.append(tot_threads)

xData = total_process
yData = total_threads
#가중치
W = tf.Variable(tf.random_uniform([1],-100,100))
# 절편
b = tf.Variable(tf.random_uniform([1],-100,100))

X = tf.compat.v1.placeholder(tf.float32)
Y = tf.compat.v1.placeholder(tf.float32)

# 가설식
H = W + X + b

cost = tf.reduce_mean(tf.square(H-Y))
a = tf.Variable(0.00025)

optimizer = tf.train.GradientDescentOptimizer(a)

train = optimizer.minimize(cost)
init = tf.compat.v1.global_variables_initializer()
sess = tf.compat.v1.Session()
sess.run(init)

for i in range(8001):
    sess.run(train, feed_dict={X: xData, Y: yData})
    if i % 1500 == 0:  # 500개 마다 모니터링
        print(i, sess.run(cost, feed_dict={X: xData, Y: yData}), sess.run(W), sess.run(b))


print(sess.run(H, feed_dict={X: [247]}))  # 프로세스의 수가 256일 때 예측되는 쓰레드의 수

saver = tf.train.Saver()
saver_path = saver.save(sess,"./saved.cpkt")

print("학습된 모델을 저장했습니다.")
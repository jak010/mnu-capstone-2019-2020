
import csv
import tensorflow as tf

x= list()
y=  list()
f = open("../csvDIR/Example01.csv","r")
rdr = csv.reader(f)
try:
    for line in rdr:
        tot_process, tot_thread = line[0].split(" ")[1],line[0].split(" ")[2]
        x.append(tot_process)
        y.append(tot_thread)
except:
    pass

xData = x # 프로세스 수
yData = y # 쓰레드 수

#가중치
W = tf.Variable(tf.random_uniform([1],-100,100))
# 절편
b = tf.Variable(tf.random_uniform([1],-100,100))

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

H = W + X + b

cost = tf.reduce_mean(tf.square(H-Y))
a = tf.Variable(0.01)
optimizer = tf.train.GradientDescentOptimizer(a)

train = optimizer.minimize(cost)
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

for i in range(5001):
    sess.run(train, feed_dict={X: xData, Y: yData})
    if i % 500 == 0:  # 500개 마다 모니터링
        print(i, sess.run(cost, feed_dict={X: xData, Y: yData}), sess.run(W), sess.run(b))

print(sess.run(H, feed_dict={X: [256]}))  # 프로세스의 수가 256일 때 예측되는 쓰레드의 수
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf

W = tf.Variable(tf.random.uniform([1],-100,100))
#가중치
# 절편
b = tf.Variable(tf.random.uniform([1],-100,100))

X =  tf.compat.v1.placeholder(tf.float32)
Y =  tf.compat.v1.placeholder(tf.float32)
# 가설 검증식
hypothesis = W + X + b

saver = tf.compat.v1.train.Saver()
model = tf.compat.v1.global_variables_initializer()

from random import randint

with tf.compat.v1.Session() as sess:
    sess.run(model)
    save_path = "../LinerMachineGener/saved.cpkt"
    saver.restore(sess, save_path)
    print("===========")



    for x in range(100):
        data = [randint(230,250)]
        ret = sess.run(hypothesis,feed_dict={X:data})
        print(data,ret)
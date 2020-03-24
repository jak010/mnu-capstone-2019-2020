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

import psutil
save_path = "../LinerMachineGener/saved.cpkt"

try:
    for x in range(20):
        with tf.compat.v1.Session() as sess:
            sess.run(model)
            saver.restore(sess, save_path)

            all_process = [x.pid for x in psutil.process_iter()]
            thread_count = 0
            for x in range(0, len(all_process)): thread_count += psutil.Process(pid=all_process[x]).num_threads()

            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

            data = [len(all_process)]
            ret = sess.run(hypothesis, feed_dict={X: data})
            print("[", data, thread_count, "]", "Predict:", ret)
except:
    pass
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import numpy as np
import tensorflow as tf

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

saver = tf.compat.v1.train.Saver()
model = tf.compat.v1.global_variables_initializer()

import psutil
save_path = "../Models/saved.cpkt"

for x in range(20):
    try:
        with tf.compat.v1.Session() as sess:
            import os
            get_pid = int(os.getpid())

            sess.run(model)
            saver.restore(sess, save_path)

            all_process = [x.pid for x in psutil.process_iter()]
            thread_count = 0
            for x in range(0, len(all_process)): thread_count += psutil.Process(pid=all_process[x]).num_threads()
            data = [thread_count]

            # process
            X1_process = [len(all_process)]
            # threads
            X2_threads = data

            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            print("Predict :", sess.run(H, feed_dict={X1: X1_process, X2: X2_threads}))

    except Exception as e:
        print(e)
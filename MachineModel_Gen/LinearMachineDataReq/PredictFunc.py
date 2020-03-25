
import os
import numpy as np
import math
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf
def call_back():
    # Model test 3
    # 가중치
    W = tf.Variable(tf.random_uniform([1], -50, 50))
    # 절편3
    b = tf.Variable(tf.random_uniform([1], -50, 50))

    X = tf.compat.v1.placeholder(tf.float32)
    Y = tf.compat.v1.placeholder(tf.float32)

    # 가설 검증식
    hypothesis = (W + 0.025 * X) + b

    saver = tf.compat.v1.train.Saver()
    model = tf.compat.v1.global_variables_initializer()

    import psutil
    save_path = "../LinerMachineGener/saved.cpkt"

    with tf.compat.v1.Session() as sess:
        sess.run(model)
        saver.restore(sess, save_path)

        all_process = [x.pid for x in psutil.process_iter()]
        thread_count = 0
        for x in range(0, len(all_process)): thread_count += psutil.Process(pid=all_process[x]).num_threads()

        data = [thread_count]

        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

        ret = int(np.round(sess.run(hypothesis, feed_dict={X: data})))  # 내림
        print("[", len(all_process), thread_count, "]", "Predict:", ret,
              sess.run(hypothesis, feed_dict={X: data}))

    return ret
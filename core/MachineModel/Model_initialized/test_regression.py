import os
# tensorflow warning message removed !
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf
import pandas as pd
import psutil
# data set define
try:
    print("=== [+] Current File Data Appending : TrainSet0===")

    dataset = pd.read_csv("../../csvDataSet/TrainSet0.csv", sep=",")

    train_process = list(dataset["process"])
    train_threads = list(dataset["threads"])
    train_memory_usage = list(dataset["memory_usage"])

    # process
    X1 = tf.compat.v1.placeholder(tf.float32, shape=[None])
    # threads
    X2 = tf.compat.v1.placeholder(tf.float32, shape=[None])

    # mem_percent
    Y = tf.compat.v1.placeholder(tf.float32, shape=[None])

    # 가중치
    W1 = tf.Variable(tf.random_normal([1], seed=1))
    W2 = tf.Variable(tf.random_normal([1], seed=1))

    # 절편3
    b = tf.Variable(tf.random_normal([1], seed=1))

    # 가설식
    H = (X1 * W1 + X2 * W2) * b

    cost = tf.reduce_mean(tf.square(H - Y))
    optimizer = tf.compat.v1.train.GradientDescentOptimizer(learning_rate=0.000000001)

    train = optimizer.minimize(cost)
    init = tf.compat.v1.global_variables_initializer()
    sess = tf.compat.v1.Session()
    sess.run(init)

    for step in range(10001):
        cost_, w1_, w2_, b_, _ = sess.run([cost, W1, W2, b, train],
                                          feed_dict={X1: train_process, X2: train_threads,
                                                     Y: train_memory_usage})

        if step % 2000 == 0:  # 500개 마다 모니터링
            print(cost_, w1_, w2_)

    import time
    from time import localtime

    cur_time = str(localtime(time.time()).tm_min) + ":" + "0" + str(localtime(time.time()).tm_sec)
    save_path = str()
    if len(cur_time.split(":")[0]) == 1:
        save_path = "../Models/saved0/saved0.cpkt"
    elif len(cur_time.split(":")[0]) == 2:
        if int(cur_time.split(":")[0][0]) == 1:
            save_path = "../Models/saved1/saved1.cpkt"
        elif int(cur_time.split(":")[0][0]) == 2:
            save_path = "../Models/saved2/saved2.cpkt"
        elif int(cur_time.split(":")[0][0]) == 3:
            save_path = "../Models/saved3/saved3.cpkt"
        elif int(cur_time.split(":")[0][0]) == 4:
            save_path = "../Models/saved4/saved4.cpkt"
        elif int(cur_time.split(":")[0][0]) == 5:
            save_path = "../Models/saved5/saved5.cpkt"
    else:
        pass

    saver = tf.compat.v1.train.Saver()
    model_file_saver = save_path
    saver_path = saver.save(sess, model_file_saver)
    print("학습된 모델을 저장했습니다.")

    try:
        saver = tf.compat.v1.train.Saver()

        all_process = [x.pid for x in psutil.process_iter()]
        thread_count = 0
        for x in range(0, len(all_process)): thread_count += psutil.Process(pid=all_process[x]).num_threads()
        data = [thread_count]

        # process
        X1_process = [len(all_process)]

        # cpu_percent
        X2_threads_usage = data
        print(X1_process, X2_threads_usage)
        print("\nPredict :", sess.run(H, feed_dict={X1: X1_process, X2: X2_threads_usage}))

        # memory usage
        predict = psutil.virtual_memory()
        print("Current Memory Percent : ", predict.percent)

    except Exception as e:
        print(e)

except Exception as e:
    print(e)



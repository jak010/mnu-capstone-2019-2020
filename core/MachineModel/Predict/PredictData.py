import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

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
H = (X1 * W1 + X2 * W2) * b

import time
import psutil

from time import localtime

cur_time = str(localtime(time.time()).tm_min) + ":" + "0" + str(localtime(time.time()).tm_sec)

save_path = str()

if len(cur_time.split(":")[0]) == 1:
    print("0분대")
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
print(save_path)

init = tf.compat.v1.global_variables_initializer()
saver = tf.compat.v1.train.Saver()

sess = tf.compat.v1.Session()
saver.restore(sess,save_path)

for x in range(20):
    all_process = [x.pid for x in psutil.process_iter()]
    thread_count = 0
    for x in range(0, len(all_process)): thread_count += psutil.Process(pid=all_process[x]).num_threads()
    data = [thread_count]

    # process
    X1_process = [len(all_process)]
    # threads
    X2_threads = data
    print(X1_process, X2_threads)
    # current Memory
    memory_usage = psutil.virtual_memory()

    predict_memory_usage = sess.run(H, feed_dict={X1: X1_process, X2: X2_threads})

    returnValue = (memory_usage.percent - predict_memory_usage) % 2

    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("\nCurrent Usage: ", memory_usage.percent, "Predict :",
          sess.run(H, feed_dict={X1: X1_process, X2: X2_threads}), "returnvalue :", returnValue)

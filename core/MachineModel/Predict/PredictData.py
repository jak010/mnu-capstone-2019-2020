import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf

#가중치
W = tf.Variable(tf.random_uniform([1],seed=1))

# 절편3
b = tf.Variable(tf.random_uniform([1],seed=1))

X = tf.compat.v1.placeholder(tf.float32)
Y = tf.compat.v1.placeholder(tf.float32)

# 가설 검증식
hypothesis = (W + 0.025*X) + b

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

            relative_counter = psutil.Process(pid=get_pid).num_threads()
            # data = [thread_count-relative_counter]

            data = [thread_count]
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

            # ret = int(np.round(sess.run(hypothesis, feed_dict={X: data})))  # 내림
            ret = sess.run(hypothesis, feed_dict={X: data})  # 내림
            print("[",thread_count, len(all_process), "]", "Predict:", ret)

    except Exception as e:
        continue
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import psutil
import numpy as np
import tensorflow as tf

from flask import *

app = Flask(__name__)

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

path = os.getcwd()
save_path = path+"/core/MachineModel/Models/saved.cpkt"

saver = tf.compat.v1.train.Saver()
model = tf.compat.v1.global_variables_initializer()

sess = tf.compat.v1.Session()
sess.run(model)

saver.restore(sess, save_path)

@app.route("/")
def index_root():
    return render_template("index.html")

@app.route("/predict",methods=['POST','GET'])
def predictAjax():
    if request.method == "POST":
        print(request.form['request'])
    try:
        all_process = [x.pid for x in psutil.process_iter()]

        thread_count = 0
        for x in range(0, len(all_process)): thread_count += psutil.Process(pid=all_process[x]).num_threads()
        data = [thread_count]

        # process
        X1_process = [len(all_process)]
        # threads
        X2_threads = data

        # current_memory_usage
        memory_usage = psutil.virtual_memory()

        # predict_cpu_usage
        predict_memory_usage = sess.run(H, feed_dict={X1: X1_process, X2: X2_threads})

        returnValue = abs((memory_usage.percent - predict_memory_usage) % 2)

        print("\n Memory Usage : ",memory_usage.percent ,"Predict Memory Usage : ",predict_memory_usage)
        print(str(returnValue[0]))
        return str(returnValue[0])

    except Exception as e:
        print(e)
        return str(0)

if __name__ == "__main__":
    app.run()


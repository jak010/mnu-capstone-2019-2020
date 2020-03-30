import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import time
import psutil
import numpy as np
import tensorflow as tf

from flask import *
app = Flask(__name__)

# 가중치
W = tf.Variable(tf.random_uniform([1], seed=1))
# 절편3
b = tf.Variable(tf.random_uniform([1], seed=1))

X = tf.compat.v1.placeholder(tf.float32)
Y = tf.compat.v1.placeholder(tf.float32)

# 가설식
H = (W + 0.025 * X) + b
path = os.getcwd()
save_path = path+"/core/MachineModel/Models/saved.cpkt"
print(save_path)
saver = tf.compat.v1.train.Saver()
model = tf.compat.v1.global_variables_initializer()

sess = tf.compat.v1.Session()
sess.run(model)

saver.restore(sess, save_path)

@app.route("/")
def index_root():
    return render_template("index.html")


@app.route("/predict",methods=["POST","GET"])
def predictAjax():
    try:
        import os
        # get_pid = int(os.getpid())

        all_process = [x.pid for x in psutil.process_iter()]
        all_process_number = len(all_process)

        thread_count = 0

        for x in range(0, len(all_process)): thread_count += psutil.Process(pid=all_process[x]).num_threads()
        data = [thread_count]

        ret = sess.run(H, feed_dict={X: data})  # 내림
        result_prec = round( (all_process_number-float(ret)) %2 ,2)

        print(result_prec , all_process_number,ret)

        # return str(cur_time)+":"+"["+str(len(all_process))+"]:"+"[Predict:" +str(ret)+"]"
        return str(result_prec)

    except Exception as e:
        return str(0)

if __name__ == "__main__":

    app.run()


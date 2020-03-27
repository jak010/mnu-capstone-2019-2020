import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import psutil
import time
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

save_path = "./MachineModel_Gen/LinerMachineGener/saved.cpkt"
saver = tf.compat.v1.train.Saver()
model = tf.compat.v1.global_variables_initializer()

sess = tf.compat.v1.Session()
sess.run(model)

saver.restore(sess, save_path)

@app.route("/")
def hello():
    return render_template("index.html", subject="안녕하세요 반갑습니다.")


@app.route("/predict",methods=["POST","GET"])
def predictAjax():
    value = request.form['predict']
    try:
        import os

        get_pid = int(os.getpid())
        all_process = [x.pid for x in psutil.process_iter()]
        thread_count = 0
        for x in range(0, len(all_process)): thread_count += psutil.Process(pid=all_process[x]).num_threads()

        data = [thread_count]

        cur_time = str(time.localtime(time.time()).tm_hour) + ":" + str(
            time.localtime(time.time()).tm_min)

        ret = np.round(sess.run(H, feed_dict={X: data}))  # 내림
        return str(cur_time)+":"+"["+str(len(all_process))+"]:"+"[Predict:" +str(ret)+"]"
    except:
        pass

if __name__ == "__main__":
    host_addr = "127.0.0.1"
    portNumber = "4040"

    app.run(host=host_addr,port=portNumber)



# os 모듈 설정은 tensorflow 라이브러리가 포함된 줄 위에 선언되야 tensorflow의 GPU 경고문이 노출되지 않습니다.
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import pandas as pd
import numpy as np
import tensorflow as tf
# from sklearn.preprocessing import MinMaxScaler

""" 이 모듈은 csvDataSet 디렉토리 밑에 있는 TrainSet0~5.csv를 학습하여 MachineModel/Models 디렉토리 밑에
학습모델을 저장하기 위해 사용합니다.

Attributes:
    _model_file_saver : 저장된 모델의 경로에서 학습된 모델을 찾아 저장합니다.
    _dataset : csvDataSet 디렉토리 밑에 TrainSet0~5.csv 에 저장된 데이터에서
                process,threads,memory_usage를 저장합니다
        _train_process : _dataset 에서 process 에 해당하는 데이터만 저장합니다.
        _train_threads : _dataset 에서 threads 에 해당하는 데이터만 저장합니다.
        _train_memory_uisage : _dataset 에서 memory_usage 에 해당하는 데이터만 저장합니다.
Args :
    void

Returns:
    이 모듈은 호출 시 학습 모델을 생성하고 호출 된 페이지로부터 성공여부의 플래그를 반환합니다.
"""

def MinMaxScaler(data):
    numerator = data - np.min(data, 0)
    denominator = np.max(data, 0) - np.min(data, 0)
    # noise term prevents the zero division
    return numerator / (denominator + 1e-5)

tf.set_random_seed(777)

X1 = tf.compat.v1.placeholder(tf.float32, shape=[None])
X2 = tf.compat.v1.placeholder(tf.float32, shape=[None])

Y = tf.compat.v1.placeholder(tf.float32, shape=[None])

W1 = tf.Variable(tf.random_normal([1], seed=1))
W2 = tf.Variable(tf.random_normal([1], seed=1))

b = tf.Variable(tf.random_normal([1], seed=1))

H = (X1 * W1 + X2 * W2) * b

cost = tf.reduce_mean(tf.square(H - Y))

optimizer = tf.compat.v1.train.GradientDescentOptimizer(learning_rate=0.00000001)

train = optimizer.compute_gradients(cost)
init = tf.compat.v1.global_variables_initializer()
sess = tf.compat.v1.Session()

sess.run(init)

for _ in range(0, 6):
    _dataset = pd.read_csv("./TrainSet" + str(_) + ".csv", sep=",")
    # scaler = MinMaxScaler(feature_range=(0,1))
    x1_train_process = MinMaxScaler(_dataset["process"].to_numpy())
    x2_train_threads = MinMaxScaler(_dataset["threads"].to_numpy())
    y_train_memory_usage = MinMaxScaler(_dataset["memory_usage"].to_numpy())

    print(x1_train_process)
    print(x2_train_threads)
    # print(y_train_memory_usage)

    for x in range(400):
        sess.run([cost, W1, W2, b], feed_dict={X1: x1_train_process, X2: x2_train_threads, Y: y_train_memory_usage})

        if(x % 200 == 0 ):
            print(sess.run(W1), sess.run(W2),b)

    # _X1 : 프로세스 ( 1차원 데이터)
    _X1_process = [0.781234]
    # _X2 : 쓰레드 수 ( 1차원 데이터)
    _X2_threads = [0.231232]

    predict_memory_usage = sess.run(H, feed_dict={X1: _X1_process, X2: _X2_threads})
    print(predict_memory_usage)

    exit()
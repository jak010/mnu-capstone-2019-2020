# os 모듈 설정은 tensorflow 라이브러리가 포함된 줄 위에 선언되야 tensorflow의 GPU 경고문이 노출되지 않습니다.
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler

class regression_init:
    @staticmethod
    def model_initalized_create(flag):
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

        train = optimizer.minimize(cost)
        init = tf.compat.v1.global_variables_initializer()
        sess = tf.compat.v1.Session()
        sess.run(init)

        _model_file_saver = "./core/MachineModel/Models/saved" + str(flag) + "/saved" + str(
            flag) + ".cpkt"

        _dataset = pd.read_csv("./core/csvDataSet/TrainSet" + str(flag) + ".csv", sep=",")

        _train_process = list(_dataset["process"])
        _train_threads = list(_dataset["threads"])
        _train_memory_usage = list(_dataset["memory_usage"])

        for step in range(10001):
            cost_, w1_, w2_, b_, _ = sess.run([cost, W1, W2, b, train],
                                              feed_dict={X1: _train_process, X2: _train_threads,
                                                         Y: _train_memory_usage})

        print(" cost : [",cost,"] train : [",_,"]" )

        saver = tf.compat.v1.train.Saver()
        saver.save(sess, _model_file_saver)

        return flag

# os 모듈 설정은 tensorflow 라이브러리가 포함된 줄 위에 선언되야 tensorflow의 GPU 경고문이 노출되지 않습니다.
import os
from time import sleep
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

""" Google Style Docstring
Attributes :
    X1 (tensorflow placeholder) : 텐서플로우 모델에서 전체 프로세스 수를 학습하기 위한 변인입니다.
    X2 (tensorflow placeholder) : 텐서플로우 모델에서 전체 쓰레드 수를 학습하기 위한 변인입니다.
    
    Y (tensorflow placeholder)  : 텐서플로우 모델에서 메모리 사용량을 학습하기 위한 변입입니다.
    
    W1 (tensorflow Variable)    : 가설식에서 X1에 적용되는 가중치입니다.
    W2 (tensorflow Variable)    : 가설식에서 X2에 적용되는 가중치입니다.
    
    H (Hypothesis)              : 선형회귀 모델에 적용할 가설식입니다. 
    
    cost (tensoflow.reduce)     : 선형회귀 모델에서 쓰일 최소 비용 값 입니다.
    optimizer(tensorflow model) : 선형회귀 (경사하강법) 모델로써 learning_rate는 0.000000001 로 주어집니다.
    
    train(tensorflow minimize)  : optimizer 객체에서 minimize() 메서드를 사용해 최소 비용값을 초기화 합니다.
    init (tensorflow iniailzed) : W1,W2의 .Variable()를 초기화 하는 데 사용합니다.
    
    sess (tensorflow Session)   : 위에 설정된 tensorflow 속성을 이용하여 tensorflow Sessions을 생성합니다.
"""
import pandas as pd
import tensorflow as tf

def model_initalized_create():
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
        이 모듈은 호출 시 학습 모델을 생성합니다.
    """
    X1 = tf.compat.v1.placeholder(tf.float32, shape=[None])
    X2 = tf.compat.v1.placeholder(tf.float32, shape=[None])

    Y = tf.compat.v1.placeholder(tf.float32, shape=[None])

    W1 = tf.Variable(tf.random_normal([1], seed=1))
    W2 = tf.Variable(tf.random_normal([1], seed=1))

    b = tf.Variable(tf.random_normal([1], seed=1))

    H = (X1 * W1 + X2 * W2) * b

    cost = tf.reduce_mean(tf.square(H - Y))
    optimizer = tf.compat.v1.train.GradientDescentOptimizer(learning_rate=0.000000001)

    train = optimizer.minimize(cost)
    init = tf.compat.v1.global_variables_initializer()
    sess = tf.compat.v1.Session()
    sess.run(init)

    for _ in range(0, 6):

        _model_file_saver = "./core/MachineModel/Models/saved" + str(_) + "/saved" + str(_) + ".cpkt"

        print("[+] Current File Data Appending : TrainSet" + str(_))

        print(_model_file_saver)

        _dataset = pd.read_csv("./core/csvDataSet/TrainSet" + str(_) + ".csv", sep=",")

        _train_process = list(_dataset["process"])
        _train_threads = list(_dataset["threads"])
        _train_memory_usage = list(_dataset["memory_usage"])

        for step in range(10001):
            cost_, w1_, w2_, b_, _ = sess.run([cost, W1, W2, b, train],
                                              feed_dict={X1: _train_process, X2: _train_threads,
                                                         Y: _train_memory_usage})
            if step % 2000 == 0:
                print(cost_, w1_, w2_)
        print("여기냐")

        saver = tf.compat.v1.train.Saver()
        saver.save(sess, _model_file_saver)

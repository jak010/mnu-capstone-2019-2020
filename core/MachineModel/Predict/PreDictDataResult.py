import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import time
import psutil
import tensorflow as tf

from time import localtime


def verifyed_model_value():
    """ 이 모듈은 학습된 모델의 메모리 사용량 예측 값의 결과를 검증하는데 사용합니다.
    Args:
        None

    Returns:
        None
    """
    cur_time = str(localtime(time.time()).tm_min) + ":" + "0" + str(localtime(time.time()).tm_sec)

    train_path = str()
    if len(cur_time.split(":")[0]) == 1:
        train_path = "/saved0/saved0.cpkt"
    elif len(cur_time.split(":")[0]) == 2:
        if int(cur_time.split(":")[0][0]) == 1:
            train_path = "/saved1/saved1.cpkt"
        elif int(cur_time.split(":")[0][0]) == 2:
            train_path = "/saved2/saved2.cpkt"
        elif int(cur_time.split(":")[0][0]) == 3:
            train_path = "/saved3/saved3.cpkt"
        elif int(cur_time.split(":")[0][0]) == 4:
            train_path = "/saved4/saved4.cpkt"
        elif int(cur_time.split(":")[0][0]) == 5:
            train_path = "/saved5/saved5.cpkt"

    model_path = "../Models" + train_path

    for _ in range(0, 6):

        print(model_path)

        init = tf.compat.v1.global_variables_initializer()
        sess = tf.compat.v1.Session()
        sess.run(init)

        saver = tf.compat.v1.train.Saver()
        saver.restore(sess, model_path)

        all_process = [x.pid for x in psutil.process_iter()]
        thread_count = 0
        for x in range(0, len(all_process)): thread_count += psutil.Process(pid=all_process[x]).num_threads()
        data = [thread_count]

        # _X1 : 프로세스 ( 1차원 데이터)
        _X1_process = [len(all_process)]
        # _X2 : 쓰레드 수 ( 1차원 데이터)
        _X2_threads = data

        print(_X1_process, _X2_threads)

        memory_usage = psutil.virtual_memory()

        # _X1 과 _X2를 입력 값으로 하여 메모리 사용량 예측하기 위함
        predict_memory_usage = sess.run(H, feed_dict={X1: _X1_process, X2: _X2_threads})

        print("\n Predict :",sess.run(H, feed_dict={X1: _X1_process, X2: _X2_threads}),"Current Usage: [", memory_usage.percent, "]" )
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")


if __name__ == '__main__':
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

    X1 = tf.compat.v1.placeholder(tf.float32, shape=[None])
    X2 = tf.compat.v1.placeholder(tf.float32, shape=[None])

    Y = tf.compat.v1.placeholder(tf.float32, shape=[None])

    W1 = tf.Variable(tf.random_normal([1], seed=1))
    W2 = tf.Variable(tf.random_normal([1], seed=1))

    b = tf.Variable(tf.random_normal([1], seed=1))

    H = (X1 * W1 + X2 * W2) * b

    verifyed_model_value()

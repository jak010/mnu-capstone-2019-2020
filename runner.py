import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import psutil
import tensorflow as tf

from flask import *
from time import localtime
from core.dataPackage.data_library import DataParsing
from core.MachineModel.Model_initialized.regression_model import regression_init
from core.ProcessCompare.ProcessTodayYesterdayCompare import DailyProcessCompare
from core.vulnerability.highestmemoryusage import TOP10Process

app = Flask(__name__)

"""
    INSTANCE INITAILIZED
"""
data_refer = DataParsing()
create_model = regression_init()

"""
    1. ROOT PAGE DECLARE 
"""


@app.route("/")
def index_root():
    return render_template("index.html")


"""
   DATA LANKED API DECLARE
"""


@app.route("/dataLanked", methods=["GET"])
def get_dataLinked():
    memoryLinked = data_refer.warning_memory_singal()
    return memoryLinked



"""
   2. DATA COLLECT API DECLARE
"""


@app.route("/dataCollecting", methods=["GET"])
def datCollectingExecute():
    value = request.args
    data_refer.data_collecting(value['flag'])
    return render_template("dataCollecting.html")


@app.route("/dataCollectValue", methods=["GET"])
def dataCollectValue():
    value = request.args
    retValue = data_refer.datacollectingChk(value['flag'])
    return retValue



""" 
    3. DATA VISUALIZED API DECLARE
"""


@app.route("/dataVisual", methods=["GET"])
def dataVisalized():
    returnGraphXY = data_refer.visualized_train_data()

    returnStatical = data_refer.visualized_train_data_statical()
    return render_template("dataVisualized.html", train_infor=returnGraphXY, train_statical=returnStatical)



"""
    4. NEW MODEL CREATE API DECLARE
"""


@app.route("/dataLearned", methods=["GET"])
def dataLearning():
    return render_template("dataLearning.html")


@app.route("/create_model", methods=["GET"])
def create_new_model():
    value = request.args.get("current_value")
    flag = create_model.model_initalized_create(value)
    return flag



"""
    5. DATA COMPARE API DECLARE
"""


@app.route("/dataCompare", methods=["GET"])
def data_compare():
    # 2020.05.04 구현 중
    file_path = app.root_path + "/core/ProcessCompare"
    dpc = DailyProcessCompare(file_path)
    processes = dpc.get_new_processes()
    print(processes)

    # view 로 보내기
    return render_template("dataCompare.html", new_processes_list=processes)



"""
    6. vulnerability API DECLARE
"""


@app.route("/vulnerability", methods=["GET"])
def vulnerability():
    # 2020.05.04 구현 중
    file_path = app.root_path + "/core/vulnerability"
    tpc = TOP10Process(file_path)
    top10 = tpc.top10_processes()
    print(top10)
    # view 로 보내기
    return render_template("vulnerability.html", top10_processes_list=top10)



"""
   **MEMORY PREDICT API DECLARE 
"""


@app.route("/predict", methods=['POST', 'GET'])
def predictAjax():
    """ 이 모돌은 index.html에서 요청한 데이터를 반환합니다. 모듈 동작 시 이 모듈에서 prcess, threads를 수집
        해서 메모리 사용량을 예측하여 반환합니다.

    Args:
        index.html에서 POST 방식의 비동기 호출로 2초마다 요청되어집니다. 현재는 '1'이라는 값 파라미터입니다.
    Return:
         메모리 사용량 반환식은
            (현재 메모리 사용량 - 예측된 메모리 사용량) 가 2보다 클 시에 2로 나눈 나머지를 리턴하고
            (현재 메모리 사용량 - 예측된 메모리 사용량) 가 2보다 작을 시에는 값을 그대로 리턴합니다. 이 결과로

            반환 값은 0과 1 사이의 값을 return 되게 만듭니다.
    """
    X1 = tf.compat.v1.placeholder(tf.float32, shape=[None])
    X2 = tf.compat.v1.placeholder(tf.float32, shape=[None])

    W1 = tf.Variable(tf.random_normal([1], seed=1))
    W2 = tf.Variable(tf.random_normal([1], seed=1))

    b = tf.Variable(tf.random_normal([1], seed=1))

    H = (X1 * W1 + X2 * W2) * b

    init = tf.compat.v1.global_variables_initializer()

    cur_time = str(localtime().tm_min) + ":" + str(localtime().tm_sec)

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

    model_path = "./core/MachineModel/Models" + train_path

    sess = tf.compat.v1.Session()
    sess.run(init)

    saver = tf.compat.v1.train.Saver()
    saver.restore(sess, model_path)

    try:
        all_process = [x.pid for x in psutil.process_iter()]

        thread_count = 0
        for x in range(0, len(all_process)): thread_count += psutil.Process(pid=all_process[x]).num_threads()
        data = [thread_count]

        X1_process = [len(all_process)]
        X2_threads = data

        memory_usage = psutil.virtual_memory()

        # predict_memory_usage
        predict_memory_usage = sess.run(H, feed_dict={X1: X1_process, X2: X2_threads})

        if abs(memory_usage.percent - predict_memory_usage) > 2:
            return_value = abs(memory_usage.percent - predict_memory_usage) % 2
        else:
            return_value = (memory_usage.percent - predict_memory_usage) % 2
        return str(return_value[0])

    except Exception as err_msg:
        return str(0)


if __name__ == "__main__":
    app.run()

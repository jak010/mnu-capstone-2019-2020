import psutil
import sys
import datetime

nowDate = datetime.datetime.now()
sys.stdout = open(nowDate.strftime('%Y-%m-%d_%H%M')+ '.txt','w')
 
 
 
def getListOfProcessSortedByMemory():
    '''
    실행 중인 프로세스 목록을 메모리 사용량별로 정렬
    '''
    listOfProcObjects = []
    # 리스트를 반복
    for proc in psutil.process_iter():
       try:
           # 프로세스 세부 정보 가져오기
           pinfo = proc.as_dict(attrs=['name'])
           pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)
           # 목록에 받아쓰기 추가
           listOfProcObjects.append(pinfo);
       except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
           pass
 
    # 주요 vms별 받아쓰기 목록 정렬(예: 메모리 사용)
    listOfProcObjects = sorted(listOfProcObjects, key=lambda procObj: procObj['vms'], reverse=True)
 
    return listOfProcObjects
 
def main():
 
    print('*** 실행 중인 모든 프로세스 목록 만들기 ***')
 
    listOfProcessNames = list()
    # 실행 중인 모든 프로세스에 대해 반복
    for proc in psutil.process_iter():
       # 사전으로 프로세스 세부 정보 가져오기
       pInfoDict = proc.as_dict(attrs=['name'])
       # 목록에 프로세스 세부사항의 받아쓰기 추가
       listOfProcessNames.append(pInfoDict)
 
    # 사전 목록을 반복하고 각 요소를 출력
    for elem in listOfProcessNames:
        print(elem)
 
 
if __name__ == '__main__':
   main()

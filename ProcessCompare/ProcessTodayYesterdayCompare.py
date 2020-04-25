import psutil
from datetime import date, timedelta
from pathlib import Path

# 프로세스 목록 저장 폴더 생성
file_folderName = "C:/Process List"
if not Path(file_folderName).is_dir():
    Path(file_folderName).mkdir()

# 프로세스 목록 파일명 생성
yesterday = date.today() - timedelta(days=1)
 
yesterday_file_name = yesterday.strftime('{}/%Y-%m-%d{}'.format(file_folderName, '.txt'))
today_file_name = date.today().strftime('{}/%Y-%m-%d{}'.format(file_folderName, '.txt'))

# 어제의 프로세스 리스트 배열에 저장하고 파일 없을 경우 생성
processes_in_yesterday = []

yesterday_file = Path(yesterday_file_name)
if yesterday_file.is_file():
    with open(yesterday_file_name, 'r') as fin_yesterday:
            processes_in_yesterday = set(line.strip() for line in fin_yesterday)
else:
    Path(yesterday_file_name).touch()

# 오늘의 프로세스 리스트 배열에 저장하고 파일 없을 경우 생성
processes_in_today = []
today_file = Path(today_file_name)
if today_file.is_file():
    with open(today_file_name, 'r') as fin_today:
            processes_in_today = set(line.strip() for line in fin_today)
else:
    Path(today_file_name).touch()

# 프로세스 목록을 메모리 샤용량순으로 가져옴
def getListOfProcessSortedByMemory():

    listOfProcObjects = []
    listUnique = []
    # 리스트를 반복
    for proc in psutil.process_iter():
        try:
            # 프로세스 세부 정보 가져오기
            pinfo = proc.as_dict(attrs=['name'])
            pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)
            # 목록에 추가
            listOfProcObjects.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
 
    # 주요 vms별 받아쓰기 목록 정렬(예: 메모리 사용)
    listOfProcObjects = sorted(listOfProcObjects, key=lambda procObj: procObj['vms'], reverse=True)
    for  element in listOfProcObjects:
        process_name = element['name']
        if process_name not in listUnique:
            listUnique.append(process_name)
    return listUnique

# 프로세스 목록 가져오는거 함수 호출 
listOfProcess  = getListOfProcessSortedByMemory()

# 지금 실행 프로세스 기존 파일에 추가하거나 생성
today_file = open(today_file_name,'a')
for elem in listOfProcess:
    if elem not in processes_in_today:
        today_file.writelines(elem+'\n')
today_file.close()

# 오늘 실행한 프로세스 - 어제 실행한 프로세스 = 어제와 비교해 오늘만 실행한 프로세스만 출력
processes_in_today = []
with open(today_file_name) as fin_today:
        processes_in_today = set(line.strip() for line in fin_today)
for process in processes_in_today:
    if process not in processes_in_yesterday:
        print(process)
 


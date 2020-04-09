#-*- coding: utf-8 -*-


import os
def port_exit_module():
    """ 이 모듈은 서버가 실행되기 전 5000번 포트를 점유 중인 PID를 종료합니다.
    Attributes :
        command (str) : 5000번 포트를 점유중인 pid를 찾기 위한 변수입니다.
        result  (str) : os.popen() 함수를 통해 결과값을 반환합니다

        kiling_port (str) : result에 저장된 값에 pid 만을 결과값으로 저장하기 위한 변수입니다.
        port_kill_command (str) : 윈도우의 cmd 명령어인 taskkill을 이용하여 pid를 종료하기 위한 문자열을 저장합니다.

        output (os.popen().read()) : port_kill_command 를 실행하여 pid를 종료시킵니다.
    Args:
        void

    Returns:
        void
    """
    for _ in range(4):
        command = " netstat -ano |find \"5000\""
        result = os.popen(command).read()

        kiling_port = result.split(" ")[-1]
        port_kill_command = "taskkill /F /pid " + kiling_port

        output = os.popen(port_kill_command).read()
        print(output)


if __name__ == '__main__':
    port_exit_module()
#-*- coding: utf-8 -*-
import os

for _ in range(4):
    command = " netstat -ano |find \"5000\""

    result = os.popen(command).read()
    print(result)

    kiling_port = result.split(" ")[-1]

    port_kill_command = "taskkill /F /pid " + kiling_port

    print(port_kill_command)

    output = os.popen(port_kill_command).read()

    print(output)


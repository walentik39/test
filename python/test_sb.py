#!/usr/bin/env python3

import dis
import subprocess
import random

def fun_ip():
    ip_list = ['8.8.4.4','127.0.1.1','test.me','ipconfig.me','8.8.8.8']
    random.shuffle(ip_list)
    for ip in ip_list:
        result = subprocess.run(
                ['ping','-c','1', ip],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                encoding="utf-8"
                )
        output = result.stderr + result.stdout
        print(output)
        if result.returncode == 0:
            print(f"Адрес {ip} пингуется")
        else:
            print(f"адрес {ip} не пингуется")
        return output    

def write_file(name):
    with open('pings.md','w') as file:
        file.write(str(name))
        dis.dis(fun_ip)

if __name__=='__main__':
    result = write_file(fun_ip())
    print(result)

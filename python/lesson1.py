#!/usr/bin/env python3

import subprocess
import random


def fun():
    result = subprocess.run(["traceroute","127.0.0.1"],stdout=subprocess.PIPE,
                            stderr=subprocess.DEVNULL,encoding='utf-8')
    return result.stdout

def fun_two():
    res = subprocess.run(["route","-FC"],stdout=subprocess.PIPE,
                         stderr=subprocess.DEVNULL,encoding='utf-8')
    return res.stdout


def file_write():
    with open('test.md','w') as f:
        f.write(str(fun()))
        f.write(str(fun_two()))
file_write()


if __name__=='__main__':
    with open('test.md','r') as file:
        reading = file.read()
        print(reading)


#!/usr/bin/env python3

import os
import subprocess
import random

def fun():
    output = subprocess.run(['ls','-l'],stderr=subprocess.DEVNULL,
                            stdout=subprocess.PIPE,encoding='utf-8')
    res = output.stdout.strip()
    return res

def main():
    x = []
    for i in range(random.randint(1,12)):
        x +=[i for i in range(2) if i%2==0]
        for j in range(random.randint(10,12)):
            x +=[j for j in range(3) if j%3==0]
            with open('test2.odt','w') as f:
                f.write(str(x))

def read_file():
    with open('test.odt','r') as fil:
        res = fil.read()
        print(res)

if __name__=='__main__':
    result = fun()
    result1 = main()
    with open('test.odt','w') as file:
        file.write(str(result))
    result2 = read_file()

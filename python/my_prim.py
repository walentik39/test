#!/usr/bin/env python3

import subprocess
import sys
import random

def fun():
    res = subprocess.run(["curl","https://api.ipify.org"],stdout=subprocess.PIPE,
                         stderr=subprocess.DEVNULL,encoding='utf-8')
    return res.stdout

def fin():
    res = subprocess.run(["curl","https://www.bbc.com/"],stdout=subprocess.PIPE,
                         stderr=subprocess.DEVNULL,encoding='utf-8')
    return res.stdout

def file_write(name):
    with open('test.odt','w') as f:
        f.write(str(name))


if __name__=='__main__':
    test = [fun(),fin()]
    ch = random.choice(test)
    file_write(ch)

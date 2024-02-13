#!/usr/bin/env python3
import random
import subprocess

def fun():
    res = subprocess.run(['host','mail.ru'],stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    return res

def file_write(name):
    with open('prim.odt','w') as fil:
        fil.write(str(name))

def fun1():
    with open('prim.odt','r+') as f:
        rs = list(f.read())
        random.shuffle(rs)
        with open('prim.odt','w') as file:
            file.write(''.join(rs))

if __name__=='__main__':
    file_write(fun())
    fun1()




#!/usr/bin/env python3

import os
import subprocess
import sys
import random

def one():
    result = subprocess.run(['ip','a'],stdout=subprocess.PIPE,
                            stderr=subprocess.DEVNULL,encoding='utf-8')
    return result.stdout

def rand_fun():
    return random.randint(0,9)

if __name__=='__main__':
    with open('prim.md','w') as file:
        file.write(str(one()))
        file.write(str(rand_fun()))
    with open('prim.md','r') as f:
        res = f.read()
        print(res)

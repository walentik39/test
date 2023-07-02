#!/usr/bin/env python3

import os
import subprocess
import sys
import random

def one():
    return subprocess.run(['ip','a'],stdout=subprocess.PIPE)

def rand_fun():
    return random.randint(0,9)

def write_file(name:str):
    with open('prim.md','w') as file:
        file.write(name)

if __name__=='__main__':
    for i in range(rand_fun()):
        write_file(str(i))
        print(i)


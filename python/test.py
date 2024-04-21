#!/usr/bin/env python3

import subprocess
def func():
    result = subprocess.run(['lsof','-i'],stdout=subprocess.PIPE,
                            stderr=subprocess.DEVNULL,encoding='utf-8')
    return result.stdout

if __name__=='__main__':
    with open('test.md','w') as f:
        f.write(str(func()))
    with open('test.md','r') as file:
        res = file.read()
        print(res)

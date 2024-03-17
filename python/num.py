#!/usr/bin/env python3

import random 
import subprocess
import os
def fun():
    result = os.system(":>test.odt")
    return result

def inner_fun():
    a = []
    for i in range(12):
        a.append(random.randint(1,50))
        a = sorted(a,key=None,reverse=False)
        with open('test.odt','a') as f:
            f.write(str(a)+'ok')
        print(a,'ok')

if __name__=='__main__':
    fun()
    inner_fun()

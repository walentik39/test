#!/usr/bin/env python3

import random
import subprocess
import os
class F:
    def fun(self):
        s = input("Введите строку: ")
        with open('test.odt','w') as f:
            f.write(s)
            f.close()    
        a = []
        for i in reversed(range(1,len(s)+1)):
            a +=[i]
            print(''.join(str(a)))

if __name__=='__main__':
    m = F()
    m.fun()

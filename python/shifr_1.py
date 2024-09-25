#!/usr/bin/env python3

import random
import subprocess
import os
class Str:
    def fun(self):
        s = input("Введите строку: ")
        with open('test.odt','w') as f:
            f.write(s)
        a = []
        for i in reversed(range(1,len(s)+1)):
            if i%2 == 0:
                a +=[i]
            print(''.join(str(a)))
            with open('test2.odt','w') as file:
                file.write(''.join(str(a)))

if __name__=='__main__':
    c = Str()
    c.fun()

#!/usr/bin/env python3

import os
import subprocess
import sys
import random
import dis

class Sub:
    def one(self):
        self.com = input("Введите команду: ")
        self.opt = input("введите опцию : ")
        result = subprocess.run([self.com,self.opt],stdout=subprocess.PIPE,
                            stderr=subprocess.DEVNULL,encoding='utf-8')
        return result

    def two(self):
        return dis.dis(self.one)

if __name__=='__main__':
    s = Sub()
    with open('prim.odt','w') as file:
        file.write(str(s.one()))
        file.write(str(s.two()))
    with open('prim.odt','r') as f:
        res = f.read()
        print(res)

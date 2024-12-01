#!/usr/bin/env python3

import os
import subprocess
class My:
    def func(self):    
        self.com = input("Введите команду: ")
        self.opt = input("опции :")

        result = subprocess.run([self.com,self.opt],stdout=subprocess.PIPE,
                            stderr=subprocess.DEVNULL,encoding='utf-8')
        return result.stdout

if __name__=='__main__':
    m = My()
    with open('test.odt','w') as f:
        f.write(str(m.func()))
    with open('test.odt','r') as file:
        res = file.read()
        print(res)

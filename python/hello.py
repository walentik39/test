#!/usr/bin/env python3

import time
import random
import os
import subprocess

class A:
    def main(self):
        os.system('lsof -i > test.odt')
        def two_main(self):
            with open('test.odt','r') as myfile:
                s = myfile.read()
                print(s)
            os.system('> test.odt')    
        return two_main(self)
class B:
    def func(self):
        res = subprocess.run(["curl","ifconfig.me"], stderr=subprocess.DEVNULL,
		stdout=subprocess.PIPE, encoding='utf-8')
        return res.stdout

    def write(self):
        with open('test.odt','a') as file:
            file.write(str(self.func()))   

	
if __name__=='__main__':
    a = A()
    b = B()
    a.main()
    b.write()


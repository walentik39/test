#!/usr/bin/env python3

import time
import random
import os

class A:
    def main(self):
        os.system('lsof -i > test.odt')
        def two_main(self):
            with open('test.odt','r+') as myfile:
                s = myfile.read()
                print(s)
            os.system('> test.odt')    
        return two_main(self)

if __name__=='__main__':
    a = A()
    a.main()


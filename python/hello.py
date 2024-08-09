#!/usr/bin/env python3

import time
import random
import os

class A:
    def main():
        os.system('lsof -i > test.odt')
        def two_main():
            with open('test.odt','r+') as myfile:
                s = myfile.read()
                print(s)
            os.system('> test.odt')    
        return two_main()
    main()

if __name__=='__main__':
    A


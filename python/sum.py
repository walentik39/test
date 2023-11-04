#!/usr/bin/env python3
import random
from math import *

class A:
    def main_func():
        a = []
        def inner_func():
            d = {}
            i = 1
            while i < 7:
                a.append(random.randint(12,454))
                x = fsum(sorted(a, key=None, reverse=True))
                d[i] = x
                print(str(d) ,end='\n')
                i += 1
        return inner_func()
    main_func()
if __name__=='__main__':
    A

#!/usr/bin/env python3
import random
from math import *

class A:
    def main_func():
        a = []
        def inner_func():
            d = {}
            for i in range(1,5):
                a.append(random.randint(12,454))
                x = fsum(sorted(a, key=None, reverse=False))
                d[i] = x
                print(d ,end='\n')
        return inner_func()
    main_func()
if __name__=='__main__':
    A

#!/usr/bin/env python3
from random import *

class Mass:
    def fun():
        a = []
        for i in range(4):
            a.append(randint(-10,500))

        for x in a: 
            for y in a:
                if(x<y):
                    x = y
                    y = x
                print(x)
if __name__=='__main__':
    Mass.fun()



#!/usr/bin/env python3

import time
import random

class A:
    def f():
        d = {}
        s = []
        i = 1
        while i < 6:
            s.append(random.randint(1,99))
            s = sorted(s, key=None, reverse=True)
            d[i] = s
            time.sleep(0.2)
            i += 1
            print(d)
    f()

if __name__=='__main__':
    A

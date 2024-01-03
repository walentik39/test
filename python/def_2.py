#!/usr/bin/env python3

import random
def func():
    x = []
    y = []
    i = 0
    while i < 7:
        x.append(random.randint(1,20))
        y.append(random.choice(x))
        print(y[::-1])
        i += 1

if __name__=='__main__':
    func()

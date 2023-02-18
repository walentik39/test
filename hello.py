#!/usr/bin/env python3

import time

s = (x ** 2 for x in range(int(input())))
for i in s:
    time.sleep(2)        
    if i%2==0:
        print(i)
    else:
        print(i ** 0.5)


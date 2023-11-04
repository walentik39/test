#!/usr/bin/env python3

from math import *
import random
def daily_sales_total(*all_sales):
    total = 0.0
    for each_sale in all_sales:
        total += float(each_sale)
    return total

def fun():
    a = 0.0
    for i in range(12):
        a += float(sqrt(random.randint(0,9)))
    return a

def fun1():
    b = 0.0
    c = [i ** 2 for i in range(12) if i%2 !=0]
    for j in c:
        b += float(sqrt(j))
    return b

if __name__=='__main__':
    result = daily_sales_total(fun(),fun1())
    print(result)

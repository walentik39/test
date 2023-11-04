#!/usr/bin/env python3

import random

def fun():
    s = input("Введите строку: ")
    a = []
    for i in reversed(range(1,len(s)+1)):
        a +=[i]
        print(''.join(str(a)))

if __name__=='__main__':
    fun()

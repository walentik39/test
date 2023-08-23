#!/usr/bin/env python3

import random

def fun():
    s = input("Введите строку: ")
    a = s.split() + list(str(random.randint(0,9)))
    print(''.join(a))
if __name__=='__main__':
    fun()

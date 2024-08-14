#!/usr/bin/env python3
import random
def fun():
    for num in range(1, 101):
        val = ''
        if num % 3 == 0:
            val += 'Fizz'
        if num % 5 == 0:
            val += 'Buzz'
        if not val:
            val = str(num)
        print(val)

if __name__=='__main__':
    fun()
        

#!/usr/bin/env python3

import random
def fun():
    a,b = 0,1
    n = random.randint(1,200)
    while a < n:
        print(a, end=' ')
        a,b = b, a+b
    print()

def main(n):
    x = []
    for i in range(random.randint(1,12)):
        x +=[i]
        with open('test.odt','w') as f:
            f.write(str(x))

def read_file():
    with open('test.odt','r') as fil:
        res = fil.read()
        print(res)

if __name__=='__main__':
    result = fun()
    result1 = main(result)
    result2 = read_file()

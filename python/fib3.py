#!/usr/bin/env python3

from typing import Dict
memo: Dict[int, int] = {0: 0, 1 : 1} # базовые случаи.

def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n -2) # мемоизация
    return memo[n]

if __name__=='__main__':
    print(fib3(int(input())))

#!/usr/bin/env python3

# рекурсия
def rec(s):
    if len(s) == 1 or len(s) == 2:
        return s
    return s[0] + '(' + rec(s[1:-1]) + ')' + s[-1]

s=input()
print(rec(s))

#!/usr/bin/env python3

a = (i ** 2 for i in range(15) if i%2 != 0)
s = []
for x in a:
    s.append(x)
    x -= 1
    s.append(x)
    print(s)

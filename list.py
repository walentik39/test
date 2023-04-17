#!/usr/bin/env python3

import random

empty_list = []
freands = ['Макс','123','Leo','John','Вера','Иван','Json']
i = 0
while i < len(freands) + 1:
    print(sorted(empty_list, key=None, reverse=False))
    empty_list.append(random.choice(freands))
    i += 1

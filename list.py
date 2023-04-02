#!/usr/bin/env python3

import random

empty_list = []
freands = ['Макс','123','Leo','John','Вера','Иван','Json']
print(freands[:2])
freands.append('Ron')
print(len(freands))
empty_list.append(random.choice(freands))
print(empty_list)

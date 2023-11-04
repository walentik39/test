#!/usr/bin/env python3

import re

s = 'AC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DC'
result = re.match('AC', s)
print(result)
result2 = re.search('DC', s)
print(result2)
result3 = re.findall('DCAC', s)
print(result3)
result4 = re.split('/', s)
print(result4)
result5 = re.split('A', s , maxsplit=5)
print(result5)
result6 = re.sub('A', 'a', s)
print(result6)
result7 = re.fullmatch('A', s)
print(result7)

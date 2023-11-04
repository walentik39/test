#!/usr/bin/env python3

import random
import requests
import socket
ip = socket.gethostname()
example = ['https://letpy.com/simple-html-example/','https://distrowatch.com','https://linux.org.ru']
result = requests.get(random.choice(example))
res = result.text.split()
s = (res[-4])
a = []
for i in s:
    if i.isdigit():
        a.append(i)
print(''.join(a))   
with open('test.odt','a') as myfile:
    myfile.write(str(sorted(a, key=None, reverse=True)))
    myfile.write(str(ip))

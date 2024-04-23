#!/usr/bin/env python3

import subprocess

def func():
    result = subprocess.run(["lsof","-i"],stdout=subprocess.PIPE,
                            stderr=subprocess.DEVNULL,encoding='utf-8')
    return result.stdout


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

if __name__=='__main__':
    with open('test.md','w') as f:
        f.write(str(func()))
    with open('test2.md','w') as fil:    
        d = list(dedupe(func()))
        fil.write(str(d))

    with open('test.md','r') as file:
        res = file.read()
        print(res)
    with open('test2.md','r') as f:
        res = f.read()
        print(res)

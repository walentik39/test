#!/usr/bin/env python3

import subprocess
import os

def ping():
    ip_list = ['8.8.4.4','https://www.freebsd.org','test.me','0.0.0.0']
    for ip in ip_list:
        result = subprocess.run(
                ['ping','-c','1','-n', ip],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                encoding="utf-8"
                )
        return result.stdout

def write():
    with open('test.md','w') as f:
        f.write(str(ping()))

if __name__=='__main__':
    write()

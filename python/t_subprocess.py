#!/usr/bin/env python3

import subprocess
import os
import random

class Sub:
    def ping(self):
        ip_list = ['8.8.4.4','https://www.freebsd.org','linux.org','0.0.0.0','192.168.100.2']
        random.shuffle(ip_list)
        for ip in ip_list:
            result = subprocess.run(
                    ['ping','-c','2', ip],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    encoding="utf-8"
                    )
            return result.stdout

    def write(self):
        with open('test.md','w') as f:
            f.write(str(self.ping()))

if __name__=='__main__':
    s = Sub()
    s.write()

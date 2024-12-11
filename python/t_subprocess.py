#!/usr/bin/env python3

import subprocess
import os
import random

class Sub:
    def ping(self):
        ip_list = ['8.8.4.4','https://www.freebsd.org','test.me','0.0.0.0']
        random.shuffle(ip_list)
        for ip in ip_list:
            result = subprocess.run(
                    ['ping','-c','1','-n', ip],
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

#!/usr/bin/env python3

import subprocess
import sys
import random

class My:
    def fun(self):
        res = subprocess.run(['ping', '-c3', 'https://api.ipify.org'],stdout=subprocess.PIPE,
                         stderr=subprocess.DEVNULL,encoding='utf-8')
        return res.stdout

    def fin(self):
        res = subprocess.run(['ping', '-c3', 'https://www.bbc.com/'],stdout=subprocess.PIPE,
                         stderr=subprocess.DEVNULL,encoding='utf-8')
        return res.stdout

    def test(self):
        t = [self.fun(), self.fin()]
        ch = random.choice(t)
        return ch


if __name__=='__main__':
    m = My()

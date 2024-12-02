#!/usr/bin/env python3

import subprocess
import random
class Rand:
    def print_rand(self):
        key = random.randint(0,256)
        a = [key]
        print(a)

class My:
    def fun(self):
        ip_list = ['8.8.4.4','127.0.1.1','test.me','0.0.0.0','8.8.8.8']
        for ip in ip_list:
            result = subprocess.run(
                ['ping','-c','1', ip],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                encoding="utf-8"
                )
                #output = result.stderr + result.stdout
                #print(output)
            if result.returncode == 0:
                print(f"Адрес {ip} пингуется")
            else:
                print(f"адрес {ip} не пингуется")

if __name__=='__main__':
    #m = My()
    #m.fun()
    r = Rand()
    r.print_rand()

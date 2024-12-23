#!/usr/bin/env python3

import random
import subprocess

class My:
    def fun(self):
        ip_list = ['8.8.4.4','freebsd.org','test.me','0.0.0.1']
        random.shuffle(ip_list)
        for ip in ip_list:
            result = subprocess.run(
                    ['ping','-c','1', ip],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    encoding="utf-8"
                    )
            output = result.stderr + result.stdout
            print(output)
        if result.returncode == 0:
            print(f"адрес {ip} пингуется")
        else:
            print(f"адрес {ip} не пингуется")
        with open('test.odt','w') as f:
            f.write(f"Адрес {ip} пингуется")

if __name__=='__main__':
    m = My()
    m.fun()

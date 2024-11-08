#!/usr/bin/env python3
import os
from threading import Thread
import subprocess
class My:
    def fun(self):
        ip_list = ['8.8.4.4','freebsd.org','test.me','0.0.0.1']
        for ip in ip_list:
            result = subprocess.run(
                ['ping','-c','1','-n', ip],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                encoding="utf-8"
                )
            output = result.stderr + result.stdout
            print(output)
        if result.returncode == 0:
            print(f"Адрес {ip} пингуется")
        else:
            print(f"адрес {ip} не пингуется")

    def some_lock(self):
        return self.fun()

if __name__=='__main__':
    m = My()
    m.some_lock()
    with open('test.md','w') as f:
        t = Thread(target=m.fun(),args=[1])
        t2 = Thread(target=m,args=[2])
        f.write(str(t))
        f.write(str(t2))

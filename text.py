#!/usr/bin/env python3

import os
class My:
    def fun():
        os.system('nmap -A mail.ru >> test.odt')
        f = open('test.odt','r+')
        os.system('cat test.odt')
        print(f)
        f.close()
fun=My.fun()

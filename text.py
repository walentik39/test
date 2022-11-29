#!/usr/bin/env python3

import os
class My:
    def fun():
        os.system('host -A mail.ru >> test.odt')
        f = open('test.odt','r+')
        os.system('cat test.odt')
        print(f)
        f.close()

if __name__=='__main__':
    fun=My.fun()

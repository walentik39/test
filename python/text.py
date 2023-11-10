#!/usr/bin/env python3

import os
import subprocess
class My:

    def fun():
        result = subprocess.run(['host','mail.ru'],stderr=subprocess.PIPE,
                                stdout=subprocess.PIPE)
        with open('test.odt','w') as file:
            file.write(str(result))

    def read_file():
        with open('test.odt','r') as file:
            for i in file:
                print(''.join(i))


if __name__=='__main__':
    My.fun()
    My.read_file()

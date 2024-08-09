#!/usr/bin/env python3

import os
import subprocess
class My(object):

    def __init__(self, file):
        self.file = file

    def set_fun(self, file):
        result = subprocess.run(['host','mail.ru'],stderr=subprocess.DEVNULL,
                                stdout=subprocess.PIPE,encoding='utf-8')
        self.file = file
        with open('test.odt','w') as file:
            file.write(str(result.stdout))

    def read_file(self, file):
        self.file = file
        with open('test.odt','r') as file:
            for i in file:
                print(''.join(i))


if __name__=='__main__':
    my = My('test.odt')
    my.set_fun('test.odt')
    my.read_file('test.odt')
    

#!/usr/bin/env python3

import subprocess
import sys

def opn():
    with open('strocka.odt','a') as file:
        r = subprocess.run(['ping','-c','1','lib.ru'],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           encoding="utf-8")
        file.write(str(r))

opn()
def main():
     with open('strocka.odt','r') as file:
        for line in file:
            print(line.rstrip())
main()



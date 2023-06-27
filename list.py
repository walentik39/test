#!/usr/bin/env python3

import random
import subprocess

def read_list(name:str) -> list:
    empty_list = []

    def names():
        freands = ['Макс','Петро','Leo','John','Вера','Иван','Json']
        for i in range(len(freands)):
            empty_list.append(random.choice(freands))
            with open('list.odt','w') as file:
                file.write(str(empty_list))
    return names()

def read_file():
    with open('list.odt') as file:
        result = file.read()
        for i in result:
            print(i.rstrip(),end=' ')


if __name__=='__main__':
    read_list('Вася')
    read_file()

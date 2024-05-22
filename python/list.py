#!/usr/bin/env python3

import random

def read_list(name:str) -> list:
    empty_list = []
    def names():
        freands = ['Злата','Макс','Пятро','Leo','John','Вера','Иван','Json']
        for i in range(len(freands)):
            empty_list.append(random.choice(freands))
            with open('list.odt','w') as f:
                f.write(str(empty_list))
                random.shuffle(empty_list)
                f.write(str(empty_list))
    return names()

def read_file():
    with open('list.odt','r') as file:
        result = file.read()
        for i in result:
            print(i.rstrip(),end=' ')


if __name__=='__main__':
    read_list(read_file())

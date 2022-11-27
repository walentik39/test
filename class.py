#!/usr/bin/env python3

class DoubleRep(object):
    def __str__(self):
        return "Hi, i am!a __str__"
    def __repl__(self):
        return "Hi, 'I am!'a__repl__"

if __name__=='__main__':
    a = DoubleRep()
    print(a)


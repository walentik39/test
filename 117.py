#!/usr/bin/env python3

string = input().replace('.',' ').replace(',',' ').split()
words = [i for i in string if i.isalnum()]
print(" ".join(words))

#!/usr/bin/env python3

import random
string = input()
if "1" in string:
    my_string = string.find("1")
    print(string[my_string:])
else:
    print(string[::-1])

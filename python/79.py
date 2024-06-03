#!/usr/bin/env python3

string = input()
if "#" in string:
    my_string = string.find("#")
    print(string[:my_string])
else:
    print(string)

#!/usr/bin/env python3

import requests

args = ["start", "-h", "-a"]

match args:
    case ["start"]:
        print("Добавте аргументы\n")
    case ["start", *arg]:
        print(f"Аргументы: {arg}")
    case ["start", input()]:
        print("Вводим свои аргуметы")

    case _:
        print(f"default: {value}")

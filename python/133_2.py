#!/usr/bin/env python3

import random
number = random.randint(0,10)
for i in range(3):
    num = int(input("Введите ваше число от 0 до 10 "))
    if num == number:
        print("Вы выиграли")
        break
    elif num < number:
        print("Загаданное число больше")
    elif num > number:
        print("Загаданное число меньше")
else:
    print("Вы проиграли")

def choice():
    numb = random.randint(0,10)
    j = 0
    while j < 11:
        rnum = int(input("Введите число от 0 до 10 "))
        if rnum == numb:
            print(" вы выиграли!")
            break
        elif rnum < numb:
            print("Загаданое число больше")
        elif rnum > numb:
            print("Загаданое число меньше")
choice()

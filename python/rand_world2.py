#!/usr/bin/env python3

import sys
import random
class RandChoice:
    def fun(self):
        last = ('Иван','Фёдр','Пилип','Андрей','"Соловей-разбойник"','Валентин','Марина','Анна','Вера','Юля','Мария')
        first = ('строитель','маляр','электрик','врач','тракторист','водитель','кранавщик','столяр','слесарь','стоматолог')
        while True:
            lastName = random.choice(last)
            firstName = random.choice(first)
            print("\n\n")
            print("{} {}".format(lastName, firstName),file=sys.stderr)
            print("\n\n")
            try_again = input("\n\nПопробуйте ещё? (Нажмите Enter либо n, чтобы выйти)\n")
            if try_again.lower() == "n":
                break

if __name__=='__main__':
    r = RandChoice()
    r.fun()

#!/usr/bin/env python3
#перевод десятичного числа (а) в двоичное (k)
a = int(input("Введите целое число: "))
k=''
while (a > 0):
    tmp = a%2
    k = str(tmp) + k
    a = a//2
print(k)

#!/usr/bin/env python3

def choose_plural(n,k):
    if n%100 in range(11, 15):
        return n, k[2]
    elif n%10 == 1:
        return n, k[0]
    elif n%10 in range(2,5):
        return n, k[1]
    return n, k[2]  

result_1 = choose_plural(23, ('копейка', 'копейки', 'копеек'))
print(result_1)
result_2 = choose_plural(7, ('рубль', 'рубля', 'рублей'))
print(result_2)
result_3 = choose_plural(51, ('цент', 'цента', 'центов'))
print(result_3)    

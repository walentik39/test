#!/usr/bin/env python3

import sys

def hook_fish():
    print('Поймал рыбу!')
    sys.exit()

def wait():
    print('Ждём...')

print('Взять червя')
print('наживить червя')
print('закинуть наживку')

while True:
    response = input('Поплавок дёрнулся? ')
    if response == 'да':
        ia_moving = True
        print('клюнуло ')
        hook_fish()
    else:
        wait()

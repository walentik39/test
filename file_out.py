#!/usr/bin/env python3

import sys
try:
    with open('test2.odt') as f:
        x = f.readline()
        for i in x:
            print(i, end='')
except IOError as e:
    print("{}\nОшибка при открытии {}. Завершение программы.". format(e, file), file=sys.stderr)
    sys.exit(1)

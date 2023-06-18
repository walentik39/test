#!/usr/bin/env python3

import subprocess
import sys
def main():
    subprocess.run(['w'])
def load():
    """ Открыть текстовый файл и вернуть список цепочек символов
    в нижнем регистре."""
    try:
        with open('test.odt') as in_file:
            loaded_txt = in_file.read().rstrip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            print(loaded_txt)
    except IOError as e:
            print("{}\nОшибка при открытии {}. Завершение программы.". format(e, file), file=sys.stderr)
            sys.exit(1)
load()
main()

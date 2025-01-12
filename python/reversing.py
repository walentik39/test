#!/usr/bin/env python3

import sys
import subprocess
class My:
    def hook_file(self):
        print('Всё работает!')
        sys.exit()

    def wait(self):
        result = subprocess.run(['lsof','-i'],stdout=subprocess.PIPE,
                            stderr =subprocess.DEVNULL,encoding='utf-8')
        with open('test.odt','w') as f:
            f.write(str(result))
        print('Ждём...')

        print('Взять червя')
        print('наживить червя')
        print('закинуть наживку')

        while True:
            response = input('Поплавок дёрнулся? ')
            if response == 'да':
                ia_moving = True
                print('клюнуло ')
                self.hook_file()
            else:
                self.wait()
if __name__=='__main__':
    m = My()
    m.wait()
    m.hook_file()

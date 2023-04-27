#!/usr/bin/env python3

import random
class A:
    def main():
        def two_main():
            x = []
            y = []
            i = 0
            while i < 7:
                x.append(random.randint(1,20))
                print(sorted(x, key=None, reverse=True),sorted(y, key=None, reverse=False))
                y.append(random.randint(1,20))
                i += 1
        return two_main()
    main()

if __name__=='__main__':
    A


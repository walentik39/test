#!/usr/bin/env python3

import random
import time
class D:
    def main():
        d = {}
        def two_main():
            i = 1
            while i < 7:
                print(d)
                time.sleep(0.1)
                d[i] = random.randint(1,100)
                i += 1
        return two_main()
    main()

if __name__=='__main__':
    D

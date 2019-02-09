#!/usr/bin/env python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    b = bin(n)
    barr = list(b[2:])
    count = 0
    total = 0

    print(barr)

    for value in barr:
        if value == '1':
            count += 1
            if total < count:
                total = count
        else:
            count = 0

    print(total)


#!/usr/bin/env python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    i = len(arr) - 1
    while i >= 0:
        print(arr[i], end=' ')
        i -= 1

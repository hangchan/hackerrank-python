#!/usr/bin/env python3
tc = int(input())

for i in range(0,tc):
    line = str(input())
    linelist = list(line)
    for ii in range(0, len(linelist), 2):
        print(linelist[ii], end='')
    print(" ", end='')
    for ii in range(1, len(linelist), 2):
        print(linelist[ii], end='')
    print("")



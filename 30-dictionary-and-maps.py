#!/usr/bin/env python3
n = int(input())
i = 0
p = {}

while i < n:
    name, number = input().split(" ")
    p[name] = number
    #print(p)
    i += 1

while True:
    try:
        search = input()
    except (EOFError):
        break
    if search in p:
        print(f"{search}={p[search]}")
    else:
        print("Not found")

import sys
from collections import deque

sys.stdin = open("./input.txt", "rt")

n = int(input())
p = dict()


for _ in range(n):
    word = input()
    p[word] = 1
for _ in range(n-1):
    word = input()
    p[word] = 0
for key, val in p.items():
    if val == 1:
        print(key)
        break


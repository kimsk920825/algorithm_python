import sys
from collections import deque

sys.stdin = open("./input.txt", "rt")

mandatory_class = input()
n = int(input())

for i in range(n):
    plan = input()
    dq = deque(mandatory_class)
    for a_class in plan:
        if a_class in dq:
            if a_class != dq.popleft():
                print("#%d No" % (i+1))
                break
    else:
        if len(dq) == 0:
            print("#%d Yes" % (i+1))
        else:
            print("#%d No" % (i+1))
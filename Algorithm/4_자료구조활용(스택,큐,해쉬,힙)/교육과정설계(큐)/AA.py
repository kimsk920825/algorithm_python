import sys
from collections import deque

sys.stdin = open("./input.txt", "rt")

mandatory_class = input()
n=int(input())
for i in range(n):
    plan=input()
    dq = deque(mandatory_class)
    print(f"디큐화: {dq}")
    for x in plan:
        if x in dq:
            print(f"dq 개별 : {x}")
            if x!=dq.popleft():
                print(f"#{i+1} NO")
                break
    else:
        if len(dq)==0:
            print(f"#{i+1} Yes")
        else:
            print(f"#{i+1} NO")
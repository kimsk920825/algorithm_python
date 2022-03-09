import sys
from collections import deque

sys.stdin = open("./input.txt", "r")
n, limit = map(int, input().split())
passenger = list(map(int, input().split()))
passenger.sort()
passenger = deque(passenger)
cnt = 0
while passenger:
    if len(passenger) == 1:
        cnt = +1
        break
    if passenger[0] + passenger[1] > limit:
        passenger.pop()
        cnt += 1
    else:
        passenger.popleft()
        passenger.pop()
        cnt += 1
print(cnt)

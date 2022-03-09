import sys

sys.stdin = open("./input.txt", "r")
n = int(input())
body = []
for i in range(n):
    height, weight = map(int, input().split())
    body.append((height, weight))
body.sort(reverse=True)
heaviest = 0
cnt = 0
for height, weight in body:
    if weight >= heaviest:
        heaviest = weight
        cnt += 1
print(cnt)

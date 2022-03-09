import sys

sys.stdin = open("./input.txt", "r")
L = int(input())
box_heights = list(map(int, input().split()))
total_loop = int(input())
for _ in range(total_loop):
    box_heights[0] += 1
    box_heights[L - 1] -= 1
    box_heights.sort()
print(box_heights[L - 1] - box_heights[0])

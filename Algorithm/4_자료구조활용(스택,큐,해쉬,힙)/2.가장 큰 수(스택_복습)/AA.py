import sys

sys.stdin = open("./input.txt", "rt")

num, m = map(int,input().split())
num = list(map(int, str(num)))
stack = []
for x in num:
    while stack and m>0 and stack[-1]<x:
        stack.pop()
        m-=1
    stack.append(x)
if m!=0:
    stack=stack[:-m]
         #stack이 비어있으면 false --> while stack --> 비어있지 않다.

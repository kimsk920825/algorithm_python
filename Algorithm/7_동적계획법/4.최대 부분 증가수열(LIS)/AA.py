import sys
sys.stdin = open("input.txt", "r")
n=int(input())
arr=list(map(int, input().split()))
arr.insert(0,0)
dy=[0]*(n+1)
dy[1] = 1
res = 0 #최대 길의의 답
for i in range(2,n+1): #1은 초기화 해두었기 때문에 2부터 돌면 된다.
    max=0
    for j in range(i-1, 0, -1): #바로 앞에서 돌아야 함.
        if arr[j]<arr[i] and dy[j] > max: #dy[j]는 
            max=dy[j]
    dy[i]=max+1
    if dy[i]>res:
        res=dy[i]



from re import M
import sys
sys.stdin=open("input.txt", "r")

def DFS(L, sum ,time):
    global res
    if time > timeLimit:
        return
    if L == numberQuestion:
        if sum > res:
            res = sum
    else:
        for i in range(numberQuestion):
            DFS(L+1, sum+pv[L], time+pt[L])
            DFS(L+1, sum, time)



if __name__=="__main__": 
    numberQuestion, timeLimit = map(int, input().split())
    pv = list()
    pt= list()
    for i in range(numberQuestion):
        points, time = map(int,input().split())
        pv.append(points)
        pt.append(time)
    res = -2147000000
    DFS(0,0,0)
    print(res)
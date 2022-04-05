import sys
sys.stdin=open("input.txt", "r")

def DFS(L):
    global cnt
    if L==n:
        for i in range(n):
            print(res[i], end = " ")
        print()
        cnt+=1
    else:
        for i in range(1, m+1):
            res[L] = i
            DFS(L+1)

if __name__=="__main__":
    m, n = map(int, input().split())
    res = [0]*n
    cnt = 0
    DFS(0)
    print(cnt)


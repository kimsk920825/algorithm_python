#n 추의 갯수
#G 각 추의 무개
#S 각 추들의 총 합 
#set() 중복을 제거하며 res에 추가
#sum 측정할 수 있는 물의 무게
#왼쪽에 물을 두면 + 오른쪽에 물을 두면 -
import sys
sys.stdin=open("input.txt", "r")

def DFS(L, sum):
    global res
    if L == n:
        if 0<sum<=s:
            res.add(sum)
    else:
        DFS(L+1, sum+G[L])
        DFS(L+1, sum-G[L])
        DFS(L+1, sum)
    
if __name__=="__main__": 
    n=int(input())
    G=list(map(int, input().split()))
    s= sum(G)
    res=set()
    DFS(0,0) 
    print(s-len(res))
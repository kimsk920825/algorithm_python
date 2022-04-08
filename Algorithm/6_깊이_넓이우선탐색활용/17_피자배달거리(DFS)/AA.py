import sys

sys.stdin=open("input.txt","r")
def DFS(L, s):
    global res
    if L==m:
        sum = 0 #도시의 피자 거리
        for j in range(len(hs)):
            x1 = hs[j][0]
            y1 = hs[j][1]
            dis = 2147000000
            for x in cb:
                x2=pz[x][0]
                y2=pz[x][1]
                dis=min(dis, abs(x1-x2)+abs(y1-y2))
            sum+=dis
        if sum < res:
            res = sum


    else:
        for i in range(s, len(pz)):
            cb[L]=i
            DFS(L+1,i+1)

if __name__ == "__main__":
    n,m=map(int, input().split()) #n:격자의 크기 , m:살아 남을 피자집의 갯수
    board= [list(map(int, input().split())) for _ in range(n)]
    hs = []
    pz = [] 
    cb=[0]*m #콤비네이션의 약자 , 조합의 경우수를 저장하는 리스트
    res = 2147000000 #답을 저장
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                hs.append((i,j))
            elif board[i][j]==2:
                pz.append((i,j))
    DFS(0,0)
    print(res)
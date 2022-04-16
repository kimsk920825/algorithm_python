#입력 
## 첫 줄: 회원의 수
## 둘째 줄: 두 개의 회원번호. 두 회원은 서로 친구라는 뜻.
#출력
## 첫 줄은 회장 후보의 점수와 회장후보 수를 출력.
## 두 번째 줄은 회장 후보를 모두 출력.
import sys
sys.stdin = open("input.txt", "r")
if __name__ == "__main__":
    n=int(input())
    dis=[[100]*(n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        dis[i][i]=0
    while True:
        a, b=map(int, input().split())
        if a==-1 and b==-1:
            break
        dis[a][b]=1
        dis[b][a]=1
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                dis[i][j]=min(dis[i][j], dis[i][k]+dis[k][j])
    res=[0]*(n+1)
    score=100
    for i in range(1,n+1):
        for j in range(1,n+1):
            res[i]=max(res[i], dis[i][j])
        score=min(score, res[i])
    out = []
    for i in range(1,n+1):
        if res[i]==score:
            out.append(i)
    print("%d %d" % (score, len(out)))
    for x in out:
        print(x, end=" ")
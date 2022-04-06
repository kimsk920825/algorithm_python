# import sys
# from collections import deque
# sys.stdin=open("input.txt", "r")
# MAX = 10000 #좌표의 맥시멈 1만
# #인덱스 번호가 좌표
# ch = [0] * (MAX+1)
# dis = [0] * (MAX+1)
# n,m = map(int, input().split())
# #n이 출발점, m이 도착점
# ch[n] = 1 
# #출발점이 n이기 때문에 ch표시를 한다.
# dis[n] = 0
# #지점은 0
# dQ=deque()
# dQ.append(n)

# while dQ: #dQ가 비워져있으면 멈춘다.
#     #now 현재 지점
#     now=dQ.popleft()
#     if now==m:
#         break
#     for next in (now-1, now+1, now+5):
#         if 0<next<=MAX:
#             if ch[next]==0:
#                 dQ.append(next)
#                 ch[next]=1
#                 dis[next]=dis[now]+1
# print(dis[m])
import sys
from collections import deque
sys.stdin=open("input.txt","r")
MAX = 10000 #좌표의 맥시멈 1만
#인덱스 번호가 좌표
ch = [0]*(MAX+1)
dis = [0]*(MAX+1)
n,m=map(int, input().split())
ch[n]=1
dis[n] = 0
dQ=deque()
dQ.append(n)

while dQ:
    now = dQ.popleft()
    print("now:",now)
    if now == m:
        break
    for next in (now-1, now+1, now+5):
        print("next:",next)
        if 0<next<=MAX:
            if ch[next]==0:
                dQ.append(next)
                ch[next]=1
                dis[next]=dis[now]+1
print(dis[m])



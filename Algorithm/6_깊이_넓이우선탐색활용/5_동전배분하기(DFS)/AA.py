#N개의 동전을 A,B,C 세명에게 나누어 주려고 합니다.
#--> 동전의 갯수 N개
#세명이 받은 동전들을 각 각 합해서 가장 큰 합이 가장 작은 합을 뺐을때의 차가 가장 적게 해봐라.
#n 동전의 갯수
#coin 각 동전을 저장하는 list
#money 각 사람의 금액
#res 차의 최소 
import sys
sys.stdin=open("input.txt", "r")

def DFS(L):
    global res
    if L == n:
        difference = max(money)-min(money)
        if difference<res:
            tmp=set()
            for x in money:
                tmp.add(x)
            if len(tmp) == 3:
                res=difference
    else:
        for i in range(3):
            money[i]+=coin[L]
            DFS(L+1)
            money[i]-=coin[L]
    
if __name__=="__main__": 
    n=int(input())
    coin = []
    money = [0]*3
    res = 2147000000
    for _ in range(n):
        coin.append(int(input()))
    DFS(0)
    print(res)
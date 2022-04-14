import sys
sys.stdin = open("input.txt", "r")
if __name__ == "__main__":
    n=int(input()) #동전의 종류 개수
    coin = list(map(int, input().split())) #동전의 종류
    m=int(input()) #
    dy=[1000]*(m+1)
    dy[0]=0
    for i in range(n):
        for j in range(coin[i], m+1):
            dy[j]=min(dy[j], dy[j-coin[i]+1])
    print(dy[m])
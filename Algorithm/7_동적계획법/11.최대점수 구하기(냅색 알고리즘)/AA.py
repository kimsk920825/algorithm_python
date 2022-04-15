import sys
sys.stdin = open("input.txt", "r")
if __name__ == "__main__":
    n,m=map(int, input().split()) #n:문제의 유형이 몇 가지인지? m: 제한 시간
    dy=[0]*(m+1)
    for i in range(n):
        #ps : problem score, pt : problem time
        ps, pt = map(int, input().split())
        for j in range(m,pt-1, -1):
            dy[j]=max(dy[j], dy[j-pt]+ps)#주어진 시간 j - 문제 푸는 시간 
    print(dy[m])
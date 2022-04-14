#17kg 무게를 저장할 수 있는 가방이 있음
#3,4,7,8,9kg의 무게를 가진 5종류의 보석이 있음
#이 보석을 가방에 담는데 17kg를 넘지 않으면서 최대의 가치가 되도록 하려면 어떻게 담아야 할까?
#한 종류의 보석을 여러 번 가방에 담을 수 있다.
#첫 번째 줄: 보석 종류와 개수와 가방에 담을 수 있는 무게의 한계값
#두 번째 줄: 각 보석의 무게와 가치

import sys
sys.stdin = open("input.txt", "r")
if __name__=="__main__":
    n, m= map(int, input().split())
    dy=[0]*(m+1)
    for i in range(n):
        w, v = map(int, input().split())
        for j in range(w, m+1):
            dy[j] = max(dy[j],dy[j-w]+v)
    print(dy[m])
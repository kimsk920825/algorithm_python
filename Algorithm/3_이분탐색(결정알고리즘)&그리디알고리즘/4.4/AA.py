import sys
sys.stdin = open("./input.txt", "r")


def Count(capacity):
    cnt = 1  # DVD갯수
    sum = 0
    for x in Music:
        if sum+x > capacity:
            cnt += 1
            sum = x
        else:
            sum+x
    return cnt


n, m = map(int, input().split())

Music = list(map(int, input().split()))
maxx = max(Music)
lt = 1  # 왼쪽
rt = sum(Music)  # 음악 사이즈 합
res = 0
while lt <= rt:
    mid = (lt+rt)//2
    if mid >= maxx and Count(mid) <= m:  # DVD1장의 용량을 mid.
        res = mid
        rt = mid-1
    else:
        lt = mid+1
print(res)

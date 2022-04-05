import sys
sys.stdin=open("input.txt", "r")

# def DFS(L):
#     if L == n+1:
#         for i in range(n+1):
#             if ch[i] == 1:
#                 print(a[i], end = " ")
#             print()
#     else:
#         ch[L] =1
#         DFS(L+1)
#         ch[L] = 0
#         DFS(L+1)
# if __name__=="__main__":
#     n = int(input())
#     a = list(map(int, input().split()))
#     ch = [0] * (n+1)
#     DFS(0)


def DFS(L,sum):
    if n == L:
        if sum == (total - sum):
            print("Yes")
            for i in range(n):
                if ch[i] == 1:
                    print(a[i], end = " ")
            sys.exit(0)
    else:
        ch[L] = 1
        DFS(L+1, sum + a[L])
        ch[L] = 0
        DFS(L+1, sum)

if __name__=="__main__":
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    ch = [0] * n
    DFS(0,0)
    print("NO")
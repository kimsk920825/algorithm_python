#십진수가 입력되면 2진수로 바꿔 출력.
#return이라고 적으면 함수를 종료시켜라라는 뜻.
import sys
sys.stdin=open("input.txt","r")
def DFS(x):
    if x==0:
        return
    else:
        DFS(x//2)
        print(x%2, end='')

if __name__=="__main__":
    n = int(input())
    DFS(n)
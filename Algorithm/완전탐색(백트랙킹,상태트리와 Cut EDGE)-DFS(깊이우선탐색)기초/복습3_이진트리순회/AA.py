#전위순회
#중위순회
#후위순회

def DFS(x):
    if x>7:
        return
    else:
        DFS(x*2)
        DFS(x*2+1)
        print(x, end=' ')

if __name__=="__main__":
    DFS(1)
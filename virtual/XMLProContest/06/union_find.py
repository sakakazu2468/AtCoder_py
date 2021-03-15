# import sys    返り値そのものに再帰を渡すと深さが増してしまう
#
# sys.setrecursionlimit(10**6)

n, q = map(int, input().split())
parents = [i for i in range(n)]  #parents[i]=iの親

def root(x):  #親をたどる再帰
    if parents[x]==x:
        return x
    else:
        # return root(parents[x])
        parents[x] = root(parents[x])
        return parents[x]

def unite(x, y): #親が違う場合、木を結合
    rx = root(x)
    ry = root(y)
    if rx!=ry:
        parents[rx] = ry


for i in range(q):
    p, a, b = map(int, input().split())
    if p==0:
        unite(a, b)
    else:
        if root(a) == root(b):
            print("Yes")
        else:
            print("No")

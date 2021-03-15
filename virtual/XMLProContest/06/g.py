n, m = map(int, input().split())
k_list = []
l_list = []
parents = [i for i in range(n+1)]
h_visited = []

def root(x):
    if parents[x]==x:
        return x
    else:
        parents[x] = root(parents[x])
        return parents[x]
    
for i in range(n):
    ipt = list(map(int, input().split()))
    k = ipt[0]
    l = ipt[1:]
    k_list.append(k)
    l_list.append(l)


ans_root = root(parents[0])
for i in range(2, n+1):
    if ans_root != root(parents[i]):
        print("NO")
        break
else:
    print("YES")


n = int(input())
d = list(map(int, input().split()))
tree_count = [0 for i in range(10**5+10)]
for i in range(n):
    tree_count[d[i]] += 1
for i in range(len(tree_count)):
    if tree_count[-1*(i+1)] != 0:
        tree_count = tree_count[:-1*(i+1)+1]
        break

if tree_count[0] != 1 or d[0] != 0:
        print(0)
else:
    ans = 1
    for i in range(1, len(tree_count)):
        for j in range(tree_count[i]):
            ans = ans*tree_count[i-1] % 998244353
    else:
        print(ans)

x, n = map(int, input().split())
p = list(map(int, input().split()))

table = [0 for i in range(102)]
for i in p:
    table[i] = 1

mx = 10000
ans = mx
dis = mx
for i in range(len(table)):
    idx = 101-i
    if (table[idx] == 0) and (dis >= abs(idx-x)):
        ans = idx
        dis = abs(idx-x)
print(ans)

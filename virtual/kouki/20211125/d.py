n, m = map(int, input().split())
x = list(map(int, input().split()))
x.sort()
dis = []
for i in range(m-1):
    dis.append(abs(x[i]-x[i+1]))
dis.sort(reverse=True)
print(sum(dis[n-1:]))

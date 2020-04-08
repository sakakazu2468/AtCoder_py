n, t = map(int, input().split())
time = 0
a = []
for i in range(n):
    a.append(int(input()))
for i in range(n):
    if i==0:
        continue
    else:
        if a[i]-a[i-1]<t:
            time += a[i]-a[i-1]
        else:
            time += t
    if i==n-1:
        time += t
print(time)

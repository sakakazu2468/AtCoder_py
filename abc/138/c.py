n = int(input())
v = list(map(int, input().split()))
v = sorted(v)
s = v[0]
for i in range(n-1):
    s = (s + v[i+1])/2
print(s)
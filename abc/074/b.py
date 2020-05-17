n = int(input())
k = int(input())
x = list(map(int, input().split()))
d = 0
for i in x:
    d += min(k-i, i)*2
print(d)


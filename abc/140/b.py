n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
point = 0
prev = -1
for i in range(n):
    point += b[a[i]-1]
    if prev+1 == a[i]:
        point += c[a[i-1]-1]
    prev = a[i]
print(point)
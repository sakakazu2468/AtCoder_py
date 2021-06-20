n, q = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
a = [0] + a + [10**18+1]
diff = [0]
diff.append(a[1]-1)
for i in range(1, n+1):
    diff.append(a[i+1]-a[i]-1)
for i in range(n+1):
    diff[i+1] += diff[i]
     
for i in range(q):
    k = int(input())
    l = 0
    r = n+1
    while True:
        m = (l+r)//2
        if diff[m] >= k:
            r = m
        else:
            l = m
        if l+1 == r:
            break
    print(a[r]-(diff[r]-k+1))




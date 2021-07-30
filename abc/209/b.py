n, x = map(int, input().split())
a = list(map(int, input().split()))
price = sum(a)-n//2
if price <= x:
    print("Yes")
else:
    print("No")

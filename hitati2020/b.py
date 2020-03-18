a, b, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
prices = []
prices.append(min(a)+min(b))
for i in range(m):
    ticket = list(map(int, input().split()))
    prices.append(a[ticket[0]-1]+b[ticket[1]-1]-ticket[2])
print(min(prices))

n = int(input())
money = 0
for i in range(n):
    x, u = input().split()
    if u == "JPY":
        money += int(x)
    elif u == "BTC":
        money += float(x)*380000
print(money)


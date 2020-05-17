n = int(input())
money = 0
for i in range(n):
    x, u = input().split()
    x = float(x)
    if u == "JPY":
        money += x
    else:
        money += x*380000
print(money)

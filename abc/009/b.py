n = int(input())
prices = []
for i in range(n):
    prices.append(int(input()))
prices = list(set(prices))
prices.remove(max(prices))
print(max(prices))

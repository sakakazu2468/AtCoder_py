a, b = map(int, input().split())
anslist = [a+b, a-b, a*b]
print(max(anslist))
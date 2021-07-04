x, y = map(int, input().split())
if x==y:
    print(x)
else:
    num = [0, 1, 2]
    num.remove(x)
    num.remove(y)
    print(num[0])
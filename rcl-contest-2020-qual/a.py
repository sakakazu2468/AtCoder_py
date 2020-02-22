n, w, k, v = map(int, input().split())
monos = []
for i in range(n):
    monos.append(tuple(map(int, input().split())))
for i in range(n):
    print(i%8)

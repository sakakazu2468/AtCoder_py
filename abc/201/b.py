n = int(input())
mountains = []
for i in range(n):
    s, t = input().split()
    mountains.append([int(t), s])
mountains.sort()
print(mountains[-2][1])

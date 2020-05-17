n = int(input())
b = []
b_i = [0 for i in range(110)]
for i in range(n):
    s = input()
    if not s in b:
        b.append(s)
        b_i[b.index(s)] += 1
    else:
        b_i[b.index(s)] += 1 
m = int(input())
for i in range(m):
    t = input()
    if not t in b:
        b.append(t)
        b_i[b.index(t)] += 1
    else:
        b_i[b.index(t)] -= 1 
print(max(b_i))

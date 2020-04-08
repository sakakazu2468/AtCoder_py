n = int(input())
table = [0 for i in range(100000+10)]
suc = 0
for i in range(n):
    a = int(input())
    if table[a] == 1:
        suc += 1
    else:
        table[a] = 1
print(suc)

l1, l2, l3 = map(int, input().split())
table = [0 for i in range(12)]

table[l1] += 1
table[l2] += 1
table[l3] += 1

for i in range(len(table)):
    if table[i] == 1 or table[i] == 3:
        print(i)

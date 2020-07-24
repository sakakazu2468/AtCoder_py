t = int(input())
table = []
for i in range(65):
    for j in range(65):
        for k in range(65):
            table.append([(2**k)*(3**j)*(5**i), [k, j, i]])
for i in range(t):
    n, a, b, c, d = map(int, input().split())
    coin_list = []
    for j in range(len(table)):
        coin = 0
        coin += abs(n-table[j][0])*d
        coin += table[j][1][0]*a
        coin += table[j][1][1]*b
        coin += table[j][1][2]*c
        coin += d
        coin_list.append(coin)
    print(min(coin_list))

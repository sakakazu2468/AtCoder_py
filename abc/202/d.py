a, b, k = map(int, input().split())

table = [[0 for i in range(b+10)] for j in range(a+10)]

for i in range(a+10):
    for j in range(b+10):
        if i==0 and j==0:
            table[0][0] = 0
        elif i==0 or j==0:
            table[i][j] = 1
        else:
            table[i][j] = table[i-1][j]*(i+j)//i


def chr_plus(ans, a_n, b_n, num):
    if num==0:
        return
    else:
        if a_n==0:
            return "b"*b_n
        elif b_n==0:
            return "a"*a_n
        elif table[a_n-1][b_n] >= num:
            return "a"+chr_plus(ans, a_n-1, b_n, num)
        else:
            num -= table[a_n-1][b_n]
            return "b"+chr_plus(ans, a_n, b_n-1, num)


print(chr_plus("", a, b, k))

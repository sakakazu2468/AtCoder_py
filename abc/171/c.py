table = []
s = 1
n = int(input())
if n <= 26:
    print(chr(n+96))
else:
    while s <= 1000000000000001:
        table.append(s)
        s *= 26

    num = 0
    sum_sum = [0]
    for i in range(len(table)-1):
        sum_sum.append(table[i+1]+sum_sum[i])
        if n <= sum_sum[i]:
            num = i
            n -= sum_sum[i-1]+1
            if n == 0:
                n += sum_sum[i-1]
            break

    ans = ""
    for i in range(num, 0, -1):
        idx = len(table)-1-i
        c = n//(table[i]-1)
        if c == 0:
            ans += "a"
        else:
            n -= c*table[i]
            ans += chr(c+96)
    print(ans)



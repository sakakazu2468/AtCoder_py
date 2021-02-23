n, k = map(int, input().split())
a = list(map(lambda x:bin(int(x))[2:].zfill(60), input().split()))

x = ""
sum_k = 0
for i in range(60):
    zero = 0
    one = 0
    for j in range(n):
        if a[j][i] == "0":
            zero += 1
        else:
            one += 1
    if zero > one:
        if sum_k + 2**(60-i-1) > k:
            x += "0"
        else:
            x += "1"
            sum_k += 2**(60-i-1)
    else:
        x += "0"

x = int("0b"+x, 0)
ans = 0
for i in range(n):
    ans += x^int("0b"+a[i], 0)
print(ans)

p = int(input())
coin = []
for i in range(1, 11):
    num = 1
    yen = 1
    for j in range(i):
        yen *= num
        num += 1
    coin.append(yen)
coin = sorted(coin, reverse=True)

ans = 0
c_num = 0
while True:
    if p//coin[c_num] > 0:
        ans += p//coin[c_num]
        p %= coin[c_num]
        c_num += 1
        if p==0:
            break
    else:
        c_num += 1
print(ans)
n = int(input())

prime = []
for i in range(2, 10**4):
    for j in range(2, i):
        if i%j == 0:
            break
    else: 
        prime.append(i)


num = [i for i in range(1, 10**7)]

for i in range(1, n+1):
    target = i
    cnt = 0
    for j in prime:
        sub_cnt = 1
        while True:
            if target%j != 0:
                break
            else:
                if sub_cnt == 0:
                    sub_cnt += 1
                sub_cnt += 1
        cnt *= sub_cnt
    num[i-1] *= cnt

print(sum[num[:n]])



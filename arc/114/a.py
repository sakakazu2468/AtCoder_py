import copy
n = int(input())
x = list(map(int, input().split()))
prime = [[0 for i in range(51)] for j in range(n)]
for i in range(n):
    for j in range(1, x[i]):
        while x[i]%(j+1)==0:
            x[i] = x[i]//(j+1)
            prime[i][j+1] += 1

prime_reverse = copy.deepcopy(prime)
for i in range(50, 0, -1):
    for j in range(n):
        if prime[j][i]!=0:
            if sum(prime[j])>prime[j][i]:
                pass
            else:
                break
    else:
        for j in range(n):
            prime[j][i] = 0

            
ans_prime = [0 for i in range(51)]
for i in range(51):
    for j in range(n):
        ans_prime[i] += prime[j][i]

ans = 1
for i in range(len(ans_prime)):
    if ans_prime[i] != 0:
        ans *= i

for i in range(50, 0, -1):
    min_num = [0 for i in range(n)]
    for j in range(n):
        if prime_reverse[j][i]!=0:
            if sum(prime_reverse[j])>prime_reverse[j][i]:
                for k in range(51):
                    if prime_reverse[j][k]!=0:
                        min_num[j] = k
                        break
            else:
                break
    else:
        for j in range(n):
            prime_reverse[j][min_num[j]] = 0

            
ans_prime_reverse = [0 for i in range(51)]
for i in range(51):
    for j in range(n):
        ans_prime_reverse[i] += prime_reverse[j][i]

ans_reverse = 1
for i in range(len(ans_prime_reverse)):
    if ans_prime_reverse[i] != 0:
        ans_reverse *= i

print(min(ans, ans_reverse))




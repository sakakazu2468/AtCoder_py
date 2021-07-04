n = int(input())
prime = []
for i in range(2, n+1):
    for j in range(2, int(i**(1/2))+1):
        if i%j == 0:
            break
        if i<j:
            continue
    else:
        prime.append(i)

ans = []
for i in range(1, n+1):
    count = 1
    num = i
    for j in range(len(prime)):
        while num%prime[j] == 0:
            num = num//prime[j]
            count += 1
        if num==1:
            break
    ans.append(count)

print(" ".join(list(map(str, ans))))

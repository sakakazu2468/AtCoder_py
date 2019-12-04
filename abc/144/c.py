n = int(input())
i = 1
ans = 10**13
while i <= n**0.5:
    if n % i == 0:
        a = i + (n//i)
        ans = min(ans, a)
    i += 1
print(ans-2)


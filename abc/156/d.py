n, a, b = map(int, input().split())

tot = 2**n-1
tot %= 10**9+7
sum_a = 1
for i in range(a):
    sum_a *= n-i
    sum_a //= i+1

sum_b = 1
for i in range(b):
    sum_b *= n-i
    sum_b %= 10**9+7
    sum_b //= i+1
    sum_b %= 10**9+7

print((tot-sum_a-sum_b)%(10**9+7))

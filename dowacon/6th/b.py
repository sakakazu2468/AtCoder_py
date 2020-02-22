from math import factorial


n = int(input())
x = list(map(int, input().split()))

kaijyo = factorial(n-1)
kaijyo_lis = [kaijyo//i for i in range(1, n)]
expect_sum = 0
kaijyo_sum = 0
for i in range(1, n):
    kaijyo_sum += kaijyo_lis[i-1]
    expect_sum += (x[i] - x[i-1]) * kaijyo_sum
print(expect_sum%(10**9+7))

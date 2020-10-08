n = int(input())
a = list(map(int, input().split()))
sub_sum = 0
for i in range(n):
    sub_sum += 1/a[i]
print(1/sub_sum)

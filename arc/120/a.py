n = int(input())
a = list(map(int, input().split()))

max_num = 0
acc_sum = 0
prev_sum = 0
for i in range(n):
    max_num = max(a[i], max_num)
    ans = 0
    ans += max_num*(i+1)
    prev_sum += a[i]
    acc_sum += prev_sum
    ans += acc_sum
    print(ans)


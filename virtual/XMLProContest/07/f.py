n = int(input())
a = list(map(int, input().split()))
sum_a = 0
same_numder = {}

same_numder[sum_a] = same_numder.get(sum_a, 0)+1
for num in a:
    sum_a += num
    same_numder[sum_a] = same_numder.get(sum_a, 0)+1

ans = 0
for count in same_numder.values():
    ans += count*(count-1)//2

print(ans)


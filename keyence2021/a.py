n, k = map(int, input().split())
a = list(map(int, input().split()))

numbers = [0 for i in range(3*10**5+10)]
for num in a:
    numbers[num] += 1

ans = 0
for i in range(len(numbers)):
    k = min(k, numbers[i])
    ans += k
print(ans)



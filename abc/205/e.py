n, m, k = map(int, input().split())
all_pattern = 1
for i in range(n+m, m-1, -1):
    all_pattern *= i
    print(all_pattern)

print(all_pattern)

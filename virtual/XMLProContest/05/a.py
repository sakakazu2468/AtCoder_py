n, a, b = map(int, input().split())
max_num = min(a, b)
min_num = max(0, max(a, b)-(n-max_num))
print(max_num, min_num)

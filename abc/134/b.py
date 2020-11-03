n, d = map(int, input().split())
spl_num = d*2+1
if not n % spl_num:
    print(n // spl_num)
else:
    print(n // spl_num + 1)
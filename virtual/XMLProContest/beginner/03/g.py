a, b, n = map(int, input().split())
rem = n%b
minus1 = n-rem-1
minus1 = max(minus1, 0)
minus1_ans = a*minus1//b - a*(minus1//b)
n_ans = a*n//b - a*(n//b)
print(max(minus1_ans, n_ans))

import math

a, b, n = map(int, input().split())
rem = n%b
minus1 = n-rem-1
minus1 = max(minus1, 0)
minus1_ans = math.floor(a*minus1/b)-a*math.floor(minus1/b)
n_ans = math.floor(a*n/b)-a*math.floor(n/b)
print(max(minus1_ans, n_ans))


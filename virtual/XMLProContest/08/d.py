a, b, n = map(int, input().split())
b_sep = n//b
x_mns1 = b_sep*b-1

max_cal = a*n//b - a*(n//b)
mns1_cal = a*x_mns1//b - a*(x_mns1//b)
if x_mns1 < 0:
    print(max_cal)
else:
    print(max(max_cal, mns1_cal))
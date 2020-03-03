a, b, c = map(int, input().split())
n = (a+b+c)/2
if n == max(a, b, c):
    print("Yes")
else:
    print("No")

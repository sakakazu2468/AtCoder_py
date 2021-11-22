n, a, b = map(int, input().split())
p = 0
for i in range(n):
    s, d = input().split()
    d = int(d)
    if d < a:
        d = a
    if d > b:
        d = b
    if s == "East":
        p += d
    else:
        p -= d
if p == 0:
    print(0)
elif p > 0:
    print("East", p)
else:
    print("West", -1*p)



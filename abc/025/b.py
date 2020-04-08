n, a, b = map(int, input().split())
place = 0
for i in range(n):
    s, d = input().split()
    d = int(d)
    if d < a:
        d = a
    elif d > b:
        d = b
    if s == "West":
        place -= d
    else:
        place += d
if place > 0:
    print("East", place)
elif place == 0:
    print(0)
else:
    print("West", -place)


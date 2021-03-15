s = input()
lose = 0
for i in s:
    if i == "x":
        lose += 1
if lose >= 8:
    print("NO")
else:
    print("YES")


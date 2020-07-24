n = int(input())
ans = [0, 0, 0, 0]
for i in range(n):
    s = input()
    if s == "AC":
        ans[0] += 1
    elif s == "WA":
        ans[1] += 1
    elif s == "TLE":
        ans[2] += 1
    else:
        ans[3] += 1
for i in range(4):
    if i == 0:
        print(f"AC x {ans[i]}")
    elif i == 1:
        print(f"WA x {ans[i]}")
    elif i == 2:
        print(f"TLE x {ans[i]}")
    else:
        print(f"RE x {ans[i]}")


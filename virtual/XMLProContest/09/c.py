n = int(input())
c = list(input())[:]
head_idx = 0
tail_idx = len(c)-1
clear = False
ans = 0
while True:
    while True:
        if c[head_idx] != "R":
            break
        head_idx += 1
        if head_idx > tail_idx:
            clear = True
            break
    while True:
        if c[tail_idx] != "W":
            break
        tail_idx -= 1
        if tail_idx < head_idx:
            clear = True
            break
    if not clear:
        ans += 1
        c[head_idx] = "R"
        c[tail_idx] = "W"
    else:
        print(ans)
        break


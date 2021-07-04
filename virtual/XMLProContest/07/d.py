n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = input()

def win(com):
    if com == "r":
        return p
    elif com == "s":
        return r
    elif com == "p":
        return s

points = 0
for i in range(k):
    idx = i
    prev = ""

    # for j in range(idx, n, k)

    while True:
        not_win = False
        if t[idx] != prev:
            points += win(t[idx])
        else:
            not_win = True
        prev = t[idx]
        idx += k
        if idx > n-1:
            break
        if not_win:
            prev = ""

print(points)

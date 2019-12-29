n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = list(input())


def point(hand):
    if hand == "r":
        return p
    elif hand == "s":
        return r
    elif hand == "p":
        return s


score = 0
for i in range(n):
    if i < k:
        score += point(t[i])
    elif k <= i and i+k < n:
        if t[i] == t[i-k] and t[i] == t[i+k]:
            if t[i-k] != "r":
                t[i] = "r"
            elif t[i-k] != "s":
                t[i] = "s"
            elif t[i-k] != "p":
                t[i] = "p"
        elif t[i] == t[i-k] and t[i] != t[i+k]:
            if t[i-k] != "r" and t[i+k] != "r":
                t[i] = "r"
            elif t[i-k] != "s" and t[i+k] != "s":
                t[i] = "s"
            elif t[i-k] != "p" and t[i+k] != "p":
                t[i] = "p"
        else:
            score += point(t[i])
    else:
        if t[i] == t[i-k]:
            if t[i-k] != "r":
                t[i] = "r"
            elif t[i-k] != "s":
                t[i] = "s"
            elif t[i-k] != "p":
                t[i] = "p"
        else:
            score += point(t[i])
print(score)

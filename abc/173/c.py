h, w, k = map(int, input().split())
c = []
for i in range(h):
    c.append(list(input())[:])

sqr = [32, 16, 8, 4, 2, 1]

def bin_num(n):
    paint_num = []
    for i in range(6):
        if n > sqr[i]:
            paint_num.append(5-i)
            n -= sqr[i]
    return paint_num 

ans = 0
h_count = 2**h
w_count = 2**w
for i in range(h_count):
    h_ng = bin_num(i+1)
    for j in range(w_count):
        w_ng = bin_num(j+1)
        count = 0
        for m in range(h):
            for l in range(w):
                if (c[m][l] == '#') and (not m in h_ng) and (not l in w_ng):
                    count += 1
        if count == k:
            ans += 1
print(ans)



a, b, k = map(int, input().split())
out = []
for i in range(k):
    if a+i > b:
        continue
    out.append(a+i)
for i in range(k):
    if b-k+i+1 < a:
        continue
    if b-k+i+1 in out:
        continue
    else:
        out.append(b-k+i+1)
for i in out:
    print(i)

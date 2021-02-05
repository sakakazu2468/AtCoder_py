n, m = map(int, input().split())
condition = []
for i in range(m):
    a, b = map(int, input().split())
    condition.append([a, b])
k = int(input())
ball = []
for i in range(k):
    c, d = map(int, input().split())
    ball.append([c, d])

decision = []
for intnum in range(2**k):
    binnum = bin(intnum)[2:]
    binnum = binnum.zfill(k)
    state = []
    for j in range(len(binnum)):
        state.append(ball[j][int(binnum[j])])
    decision.append(state)

max_satis = -1
for i in range(len(decision)):
    satis = 0
    for j in range(len(condition)):
        if (condition[j][0] in decision[i]) and (condition[j][1] in decision[i]):
            satis += 1
    max_satis = max(max_satis, satis)

print(max_satis)

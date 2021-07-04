n, x = map(int, input().split())
mdonut = 10**5
for i in range(n):
    m = int(input())
    mdonut = min(m, mdonut)
    x -= m

print(n+(x//mdonut))

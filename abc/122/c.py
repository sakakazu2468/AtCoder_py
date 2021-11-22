n, q = map(int, input().split())
s = input()

acs = [0]
prev = ""
for i in range(n):
    ac = 0
    if prev=="A" and s[i] == "C":
        ac = 1
    acs.append(acs[-1]+ac)
    prev = s[i]

for i in range(q):
    l, r = map(lambda x: int(x)-1, input().split())
    ans = acs[r+1]-acs[l]
    if l != 0:
        if s[l] == "C" and s[l-1] == "A":
            ans -= 1
    print(ans)
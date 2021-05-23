n = int(input())
s = input()
l = 0
r = 0
lp = 0
rp = 0
for i in range(len(s)):
    if s[i] == '(':
        if r != 0:
            if r > l:
                lp += r-l
            elif l > r:
                rp += l-r
            l, r = 0, 0
        l += 1
    if s[i] == ')':
        r += 1

if r > l:
    lp += r-l
elif l > r:
    rp += l-r
print('('*lp+s+')'*rp)

s = input()
n = len(s)

calc = False
ans = 0
left = 0
right = 0
for i in range(n):
    if i == n-1:
        if s[i] == '<':
            left += 1
            calc = True
        else:
            right += 1
            calc = True
    else:
        if s[i] == '<':
            left += 1
        else:
            right += 1
            if s[i+1] == '<':
                calc = True
    if calc:
        if left >= right:
            ans += left*(left+1)//2
            ans += right*(right-1)//2
            calc = False
            left = 0
            right = 0
        else:
            ans += right*(right+1)//2
            ans += left*(left-1)//2
            calc = False
            left = 0
            right = 0

print(ans)

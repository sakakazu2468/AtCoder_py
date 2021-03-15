n = input()
ans = 0

for i in range((len(n)-1)//3):
    ans += int(n) - (10**((i+1)*3)-1)
print(ans)

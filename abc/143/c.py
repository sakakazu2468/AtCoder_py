n = int(input())
s = input()
num = 1
for i in range(n-1):
    if s[i] == s[i+1]:
        continue
    else:
        num += 1
print(num)

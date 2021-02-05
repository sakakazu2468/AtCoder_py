n = int(input())
strinfo = [[0 for i in range(26)] for i in range(n)]
for i in range(n):
    a = input()
    for ch in a:
        strinfo[i][ord(ch)-97] += 1

same_chr = [0 for i in range(26)]
for i in range(26):
    min_chr = 100000
    for j in range(n):
        min_chr = min(strinfo[j][i], min_chr)
    same_chr[i] = min_chr

ans = ""
for i in range(26):
    for j in range(same_chr[i]):
        ans += chr(i+97)
print(ans)



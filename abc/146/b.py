n = int(input())
s = input()
ans = ""

for i in s:
    num = ord(i) + n
    while num > 90:
        num -= 26
    ans += chr(num)
print(ans)


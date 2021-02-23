import re
s = input()
result = re.finditer(r"(25)+",s)
l_25 = [len(i.group(0))//2 for i in result]
ans = sum(int(i/2 * (i+1)) for i in l_25)
print(ans)

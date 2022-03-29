n = int(input())
s = input()
char = set()
for c in s:
    char.add(c)
l = len(char)
print(l*(l-1)*(l-2))

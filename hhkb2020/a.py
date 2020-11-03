s = input()
t = input()
if s == 'Y' and ord(t) > 90:
    print(chr(ord(t)-32))
else:
    print(t)
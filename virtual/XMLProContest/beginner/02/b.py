a, b, c, d = map(int, input().split())
takahashi = b*c
aoki = a*d
if takahashi > aoki:
    print("TAKAHASHI")
elif takahashi < aoki:
    print("AOKI")
else:
    print("DRAW")

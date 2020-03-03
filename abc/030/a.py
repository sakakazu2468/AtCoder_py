a, b, c, d = map(int, input().split())

taka = b/a
ao = d/c

if taka > ao:
    print("TAKAHASHI")
elif taka == ao:
    print("DRAW")
else:
    print("AOKI")

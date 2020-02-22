a, b, c = map(int, input().split())
if a==b or a==c or b==c:
    if not(a==b and a==c and b==c):
        print("Yes")
    else:
        print("No")
else:
    print("No")

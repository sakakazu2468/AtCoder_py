a, b = input().split()
n = int(a+b)
for i in range(1000):
    if i**2 == n:
        print("Yes")
        break
else:
    print("No")

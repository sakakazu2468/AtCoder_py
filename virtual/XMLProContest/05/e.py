n = int(input())
tri = [0]*(10**6)
tri[0] = 0
tri[1] = 0
tri[2] = 1
if n == 1:
    print(tri[0])
elif n == 2:
    print(tri[1])
elif n == 3:
    print(tri[2])
else:
    for i in range(3, n):
        tri[i] = (tri[i-1] + tri[i-2] + tri[i-3])%10007
    print(tri[n-1])


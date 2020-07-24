n = int(input())
xyz = [[[0 for i in range(101)] for j in range(101)] for k in range(101)]
ans = [0 for i in range(n+1)]

def gen_n(x, y, z):
    return x**2 + y**2 + z**2 + x*y + y*z + z*x
for i in range(1, 101):
    for j in range(1, 101):
        for k in range(1, 101):
            num = gen_n(i, j, k)
            if n >= num:
                ans[num] += 1
for i in range(1, n+1):
    print(ans[i])

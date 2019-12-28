n = int(input())
for i in range(50000):
    p = int(i*0.08)+i
    if p == n:
        print(i)
        break
    if p > n:
        print(":(")
        break

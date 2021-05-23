s = 0
for i in range(1, 10):
    for j in range(1, 10):
        s += i*j

n = int(input())
diff = s-n
for i in range(1, 10):
    for j in range(1, 10):
        if diff == i*j:
            print(f"{i} x {j}")



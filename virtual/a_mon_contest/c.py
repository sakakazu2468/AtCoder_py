n = int(input())
a = 0
b = n
m = 1000000
for i in range(n//2):
    a += 1
    b -= 1
    s = sum(list(map(int, list(str(a))))) + sum(list(map(int, list(str(b)))))
    m = min(m, s)
print(m)

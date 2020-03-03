a = int(input())
b = int(input())
n = int(input())

s = a*b
while b:
    a, b = b, a%b

s //= a
p = s
while n > s:
    s += p

print(s)

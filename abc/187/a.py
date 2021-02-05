a, b = map(int, input().split())
a_sum = 0
for i in str(a):
    a_sum += int(i)
b_sum = 0
for i in str(b):
    b_sum += int(i)
print(max(a_sum, b_sum))



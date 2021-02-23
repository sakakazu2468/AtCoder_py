n = int(input())
power = 1
for i in range(n):
    power = (power*(i+1))%(10**9+7)
print(power)


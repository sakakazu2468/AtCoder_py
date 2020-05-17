import math 


x = int(input())
m = 100
y = 0
while x > m:
    y += 1
    m = m + math.floor(m*0.01)
print(y)


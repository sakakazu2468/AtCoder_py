import math


a, b, h, m = map(int, input().split())
m_dig = 6*m
h_dig = 30*h + m*0.5
angle = abs(m_dig-h_dig)
cosa = math.cos(math.radians(angle))
ans_2 = a**2 + b**2 - 2*a*b*cosa
print(math.sqrt(ans_2))

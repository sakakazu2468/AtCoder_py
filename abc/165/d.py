import math 


a, b, n = map(int, input().split())
if b > n:
    x = n    
else:
    x = b-1
print(math.floor(a*x/b)-a*math.floor(x/b))

n = int(input())
ans = []
for i in range(n//2+1):
    h = i+1
    v = n//h
    rem = n-h*v
    ans.append(abs(h-v)+rem)
print(min(ans))


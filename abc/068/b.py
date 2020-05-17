n = int(input())

def div(x):
    global count
    if x%2==1:
        return count
    else:
        count += 1
        return div(x//2)
m = -1
for i in range(n):
    count = 0
    r = div(i+1)
    if m < r:
        m = r
        ans = i+1

print(ans)

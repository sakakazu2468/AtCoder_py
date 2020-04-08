h = int(input())
dep = 0
def log_num(n):
    global dep
    if n == 1:
        return dep
    else:
        dep += 1
        log_num(n//2)
log_num(h)
ans = 1
for i in range(dep+1):
    ans *= 2
print(ans-1)

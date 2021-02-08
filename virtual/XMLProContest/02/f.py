n, q = map(int, input().split())
othello = [0 for i in range(n)]
for i in range(q):
    l, r = map(int, input().split())
    othello[l-1] += 1
    if r != n:
        othello[r] -= 1
        
ans = ""
state = 0
for i in othello:
    state += i
    if state%2 == 0:
        ans += '0'
    else:
        ans += '1'

print(ans)
        

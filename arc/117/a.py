a, b = map(int, input().split())
a_rem = 10**9
b_rem = 10**9
ans = []
for i in range(a-1):
    ans.append(i+1)
    a_rem -= i+1
ans.append(a_rem)

for i in range(b-1):
    ans.append(-1*(i+1))
    b_rem -= i+1
ans.append(-1*b_rem)

for i in range(len(ans)):
    if i == len(ans)-1:
        print(ans[i])
    else:
        print(ans[i], end=" ")


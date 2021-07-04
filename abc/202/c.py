n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a_list = [0 for i in range(n)]
for i in a:
    a_list[i-1] += 1

c_list = [0 for i in range(n)]
for i in c:
    c_list[b[i-1]-1] += 1

ans = 0
for i in range(n):
    ans += a_list[i]*c_list[i]

print(ans)

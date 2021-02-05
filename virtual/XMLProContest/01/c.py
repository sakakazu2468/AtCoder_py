n = int(input())
a = list(map(int, input().split()))
num_table = [0 for i in range(10**5+10)]
for i in range(n):
    num_table[a[i]] += 1
    num_table[a[i]+1] += 1
    num_table[a[i]+2] += 1
# ans = -1
# for i in range(len(num_table)):
#     ans = max(ans, num_table[i])
# print(ans)

print(max(num_table))

n = int(input())
a = list(map(int, input().split()))
a.sort()
a_dic = {}
for i in range(n):
    a_dic[a[i]] = a_dic.get(a[i], 0) + 1
rm = 0
for value in a_dic.values():
    rm += value - 1

if rm%2!=0:
    rm += 1
print(n-rm)

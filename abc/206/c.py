n = int(input())
a = list(map(int, input().split()))
ap = n*(n-1)//2
a_dic = {}
for i in a:
    a_dic[i] = a_dic.get(i, 0) + 1
for v in a_dic.values():
    ap -= v*(v-1)//2
print(ap)

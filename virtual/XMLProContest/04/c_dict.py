n = int(input())
d = list(map(int, input().split()))
m = int(input())
t = list(map(int, input().split()))

d_dict = {}
t_dict = {}
for i in d:
    d_dict[i] = d_dict.get(i, 0) + 1
for i in t:
    t_dict[i] = t_dict.get(i, 0) + 1

for key, value in t_dict.items():
    d_pop = d_dict.get(key, 0)
    if d_pop < value:
        print("NO")
        break
else:
    print("YES")

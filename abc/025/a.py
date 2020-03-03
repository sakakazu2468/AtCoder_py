s = list(input())
n = int(input())

s_list = []
for i in range(5):
    for j in range(5):
        s_list.append(s[i]+s[j])
s_list.sort()

print(s_list[n-1])

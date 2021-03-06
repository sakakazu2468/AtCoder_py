sort_list = sorted(list(map(int, input().split())))
if ((sort_list[2]-sort_list[0])+(sort_list[2]-sort_list[1]))%2 == 0:
    target = sort_list[2]
else:
    target = sort_list[2]+1

count = 0
for i in range(3):
    count += (target-sort_list[i])//2
    sort_list[i] += (target-sort_list[i]//2)*2
if (sort_list[0] == sort_list[1]) and (sort_list[1] == sort_list[2]):
    print(count)
else:
    print(count+1)

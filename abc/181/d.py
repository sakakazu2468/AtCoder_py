s = input()


eights = []
if len(s) >= 3:
    for i in range(12, 124):
        eights.append((i+1)*8)
elif len(s) == 2:
    for i in range(1, 124):
        eights.append((i+1)*8)
else:
    for i in range(124):
        eights.append((i+1)*8)

eights_num_list = []
for i in eights:
    num_str = str(i)
    num_count = [0 for i in range(10)]
    for j in num_str:
        num_count[int(j)] += 1
    eights_num_list.append(num_count)


input_num_count = [0 for i in range(10)]
for i in s:
    input_num_count[int(i)] += 1


flag = False
for i in eights_num_list:
    for j in range(10):
        if i[j] > input_num_count[j]:
            break
    else:
        flag = True
if flag:
    print("Yes")
else:
     print("No")


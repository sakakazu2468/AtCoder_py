h, w, a, b = map(int, input().split())
all_list = [0, 1, 2, 3, 18, 9, 36]
max_pattern = 0
if h*w == 1:
    max_pattern = all_list[0]
    list_num = 0
elif h*w == 2:
    max_pattern = all_list[1]
    list_num = 1
elif h*w == 4:
    max_pattern = all_list[2]
    list_num = 4
elif h*w == 6:
    max_pattern = all_list[3]
    list_num = 7
elif h*w == 9:
    max_pattern = all_list[4]
    list_num = 12
elif h*w == 12:
    max_pattern = all_list[5]
    list_num = 17
elif h*w == 16:
    max_pattern = all_list[6]
    list_num = 24

if a==0:
    print(1)
elif a==1:
    print(list_num)
else:
    for i in range()



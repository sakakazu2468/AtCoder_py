n = input()
rem = 0
all_sum = 0
rem_list = [0, 0, 0]
for i in n:
    rem_list[int(i)%3] += 1
if rem_list[0]==0:
    if rem_list[1]==0 and rem_list[2]<=2:
        print(-1)
    elif rem_list[2]==0 and rem_list[1]<=2:
        print(-1)
    else:
        print(min(abs(rem_list[1]-rem_list[2])%3, rem_list[1]%3, rem_list[2]%3))
else:
    if rem_list[2]%3==0:
        print(min(abs(rem_list[1]-rem_list[2])%3, rem_list[1]%3))
    elif rem_list[1]%3==0:
        print(min(abs(rem_list[1]-rem_list[2])%3, rem_list[2]%3))
    else:
        print(min(abs(rem_list[1]-rem_list[2])%3, rem_list[1]%3, rem_list[2]%3))

s = input()
l = len(s)
anslist = [0 for i in range(l)]
sum_count = 0
mode = False
for i in range(l):
    if mode == True and s[i] == 'R':
        if not sum_count % 2:
            anslist[conc_num1] += int(sum_count/2)
            anslist[conc_num2] += int(sum_count/2)
        else:
            if not o_e_num % 2:
                anslist[conc_num1] += int(sum_count//2+1)
                anslist[conc_num2] += int(sum_count//2)
            else:
                anslist[conc_num1] += int(sum_count//2)
                anslist[conc_num2] += int(sum_count//2+1)
        mode = False
        sum_count = 0
    sum_count += 1
    if mode == False and s[i] == 'L':
        conc_num1 = i-1
        conc_num2 = i
        o_e_num = sum_count
        mode = True
if not sum_count % 2:
    anslist[conc_num1] += int(sum_count/2)
    anslist[conc_num2] += int(sum_count/2)
else:
    if not o_e_num % 2:
        anslist[conc_num1] += int(sum_count//2+1)
        anslist[conc_num2] += int(sum_count//2)
    else:
        anslist[conc_num1] += int(sum_count//2)
        anslist[conc_num2] += int(sum_count//2+1)
for i in range(len(anslist)):
    print(anslist[i], end = ' ')
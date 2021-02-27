a, b = input().split()
ans_list = [0 for _ in range(100)]
a_list = list(a[:])
# b = str(int(b[0]+b[2:]))
b = str(int(float(b)*100))
print(b)
for i in range(len(b)):
    b_num = int(b[-1-i])
    plusnum = 0
    for j in range(len(a)):
        a_num = int(a[-1-j])
        a_num += plusnum
        mult = a_num*b_num
        if len(str(plusnum)) >= 2:
            plusnum = int(str(mult)[0])
            ans_list[i+j] += int(str(mult)[1])
        else:
            plusnum = 0
            ans_list[i+j] += mult

for i in range(len(ans_list)):
    for j in range(1, len(str(ans_list[i]))):
        ans_list[i+j] += int(str(ans_list[i])[-j-1])
    ans_list[i] = int(str(ans_list[i])[-1])

ans = ""
for i in range(len(ans_list)):
    ans += str(ans_list[-i-1])
print(int(ans)//100)

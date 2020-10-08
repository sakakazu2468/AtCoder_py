n = int(input())
s_list = [0 for i in range(10**5)]
one = 0
for i in range(n):
    s = list(input())
    count = 0
    for j in range(10):
            count += 2**ord(s[j])
    if s_list[count] == 0:
        one += 1
    elif s_list[count] == 1:
        one -= 1
    s_list[count] += s_list[count] + 1
print(sum(s_list)-one)
n = int(input())
s = input()
q = int(input())
s_list_1 = [ord(i) for i in s]
s_list_2 = s_list_1[n:]
s_list_1 = s_list_1[:n]
for i in range(q):
    t, a, b = map(int, input().split())
    if t==1:
        if a > n and b > n:
            tmp = s_list_2[a-n-1]
            s_list_2[a-n-1] = s_list_2[b-n-1]
            s_list_2[b-n-1] = tmp
        elif b > n:
            tmp = s_list_1[a-1]
            s_list_1[a-1] = s_list_2[b-n-1]
            s_list_2[b-n-1] = tmp
        else:
            tmp = s_list_1[a-1]
            s_list_1[a-1] = s_list_1[b-1]
            s_list_1[b-1] = tmp
    else:
        tmp_list = s_list_1[:]
        s_list_1 = s_list_2[:]
        s_list_2 = tmp_list[:]

for i in s_list_1:
    print(chr(i), end="")
for i in s_list_2:
    print(chr(i), end="")
print()

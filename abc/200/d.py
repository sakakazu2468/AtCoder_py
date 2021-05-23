n = int(input())
a = list(map(int, input().split()))
a_mod = [a[i]%200 for i in range(n)]
a_set = set(a_mod)
end = False
if len(a_mod) != len(a_set):
    for i in range(n):
        for j in range(n):
            if i == j:
                break
            if a_mod[i] == a_mod[j]:
                print("Yes")
                print(1, i+1)
                print(1, j+1)
                end = True
                break
        if end:
            break
else:
    a_idx = [[a_mod[i], i] for i in range(n)]
    a_idx.sort()
    all_pattern = []
    pattern_detail = [[] for i in range(20000)]
    exist = False

    for i in range(n):
        num = a_idx[i][0]
        if num in all_pattern:
            b = pattern_detail[num]
            c = [num]
            exist = True
            break
        all_pattern.append(num)
        pattern_detail[num] = [num]
        for j in range(len(all_pattern)-1):
            new_num = all_pattern[j] + num
            if new_num%200 in all_pattern:
                b = pattern_detail[new_num%200]
                c = pattern_detail[all_pattern[j]] + [num]
                exist = True
                break
            all_pattern.append(new_num)
            pattern_detail[new_num] = pattern_detail[all_pattern[j]] + [num]
        if exist:
            break

    if exist:
        b_ans = []
        for i in range(len(b)):
            for j in range(n):
                if b[i] == a_idx[j][0]:
                    b_ans.append(a_idx[j][1])
        b_ans.sort()
        c_ans = []
        for i in range(len(c)):
            for j in range(n):
                if c[i] == a_idx[j][0]:
                    c_ans.append(a_idx[j][1])
        c_ans.sort()

        print("Yes")
        print(len(b_ans), end=" ")
        for i in range(len(b_ans)):
            print(b_ans[i]+1, end=" ")
        print()
        print(len(c_ans), end=" ")
        for i in range(len(c_ans)):
            print(c_ans[i]+1, end=" ")
        print()
    else:
        print("No")


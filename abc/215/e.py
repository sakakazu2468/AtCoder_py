n = int(input())
s = input()

def mod(x):
    return x%998244353

ans = 1
for i in range(n):
    ans = mod(ans*2)

ans -= 1

flag_list = []
for ch in "ABCDEFGHIJ":
    prev = ""
    cont = [0]
    flag = []
    count = 0
    for ss in s:
        if prev != ch:
            if ss != ch:
                cont[-1] += 1
            else:
                cont.append(1)
                flag.append(count)
        else:
            if ss != ch:
                cont.append(1)
            else:
                cont[-1] += 1
        count += 1
    flag_list.append(flag)

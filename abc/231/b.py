n = int(input())
dic = dict()
for i in range(n):
    ipt = input()
    dic[ipt] = dic.get(ipt, 0) + 1

ans = 0
ans_key = 0
for key, val in dic.items():
    if ans < val:
        ans = val
        ans_key = key
print(ans_key)


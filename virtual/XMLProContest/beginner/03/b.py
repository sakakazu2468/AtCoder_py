s = input()
dic = {}
for i in s:
    dic[i] = dic.get(i, 0) + 1
for val in dic.values():
    if val >= 2:
        print("no")
        break
else:
    print("yes")


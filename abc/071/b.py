s = input()
abc = [chr(i+97) for i in range(26)]
for i in s:
    if i in abc:
        abc.remove(i)
if abc:
    print(min(abc))
else:
    print("None")

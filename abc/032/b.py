s = input()
k = int(input())
count = 0
if len(s) < k:
    print(0)
else:
    word = []
    for i in range(len(s)-k+1):
        if s[i:i+k] in word:
            pass
        else:
            count += 1
            word.append(s[i:i+k])
    print(count)

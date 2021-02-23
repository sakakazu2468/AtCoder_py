n = int(input())
march = [0 for _ in range(5)]
for i in range(n):
    s = input()
    if s[0] == "M":
        march[0] += 1
    elif s[0] == "A":
        march[1] += 1
    elif s[0] == "R":
        march[2] += 1
    elif s[0] == "C":
        march[3] += 1
    elif s[0] == "H":
        march[4] += 1

ans = 0
for i in range(4):
    for j in range(4-i):
        march_index = [0, 1, 2, 3, 4]
        march_index.remove(i)
        march_index.remove(i+j+1)
        choice = 1
        for cnt in march_index:
            choice *= march[cnt]
        ans += choice
print(ans)



        



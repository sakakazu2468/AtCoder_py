n = int(input())
contest = [int(str(i)+str(i)+str(i)) for i in range(1, 10)]
for i in range(9):
    if n <= contest[i]:
        print(contest[i])
        break

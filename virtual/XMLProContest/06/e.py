n, l = map(int, input().split())

amida = []
for i in range(l):
    ipt = list(input())[:]
    amida.append(ipt)

goal = list(input())[:]
for i in range(len(goal)):
    if goal[i] == "o":
        goal_num = i
        break

for i in range(l-1, -1, -1):
    if goal_num != (n-1)*2:
        if amida[i][goal_num+1] == "-":
            goal_num += 2
            continue
    if goal_num != 0:
        if amida[i][goal_num-1] == "-":
            goal_num -= 2
print(goal_num//2+1)

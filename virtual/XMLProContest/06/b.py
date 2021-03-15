n = int(input())
plan = []
for i in range(n):
    plan.append(list(map(int, input().split())))

pos_x = 0
pos_y = 0
plan_num = 0
plan_t = plan[plan_num][0]
plan_x = plan[plan_num][1]
plan_y = plan[plan_num][2]
for i in range(1, 10**5+1):
    if pos_x < plan_x:
        pos_x += 1
    elif pos_x > plan_x:
        pos_x -= 1
    elif pos_y < plan_y:
        pos_y += 1
    elif pos_y > plan_y:
        pos_y -= 1
    else:
        pos_x += 1
    
    if i == plan_t:
        if (pos_x == plan_x) and (pos_y == plan_y):
            plan_num += 1
            if plan_num >= n:
                continue
            plan_t = plan[plan_num][0]
            plan_x = plan[plan_num][1]
            plan_y = plan[plan_num][2]
        else:
            print("No")
            break
else:
    print("Yes")


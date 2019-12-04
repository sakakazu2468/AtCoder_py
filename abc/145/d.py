x, y = map(int, input().split())

way = y*2-x
away = x*2-y
if way >= 0 and way%3 == 0 and away >= 0 and (x+y)%3 == 0:
    var_y = way//3
    var_x = (x-var_y)//2
    ans = 1
    con = var_y + var_x
    top = min(var_y, var_x)
    for i in range(top-):
        ans*=con-i
        ans %= 10**9+7
    print(ans)
else:
    print(0)

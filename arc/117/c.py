n = int(input())
c = input()
keisu = 1
pascal_sum = 0

def color_num(c):
    if c=="B":
        return 0
    elif c=="W":
        return 1
    elif c=="R":
        return 2

for i in range(n):
    pascal_sum += (keisu * color_num(c[i]))%3
    pascal_sum = pascal_sum%3
    keisu = keisu*(n-(i+1))//(i+1)

ans = pascal_sum%3
if n%2==0:
    ans = (3-ans)%3

if ans == 0:
    print("B")
elif ans == 1:
    print("W")
else:
    print("R")

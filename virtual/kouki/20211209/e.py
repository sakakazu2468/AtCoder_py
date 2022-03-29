x = int(input())
dis = 0
for i in range(1, 10**5):
    dis += i
    if dis >= x:
        print(i)
        break

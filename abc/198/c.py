r, x, y = map(int, input().split())
dis = x**2 + y**2
for i in range(2*10**5):
    if (r*(i+1))**2 >= dis:
        print(i+1)
        break


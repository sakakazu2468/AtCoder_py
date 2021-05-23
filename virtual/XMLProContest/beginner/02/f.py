a = int(input())

def f(x):
    total = 0
    str_x = str(x)
    for i in range(len(str_x)):
        total += x**i * int(str_x[-1*(i+1)])
    return total

for i in range(10, 10001):
    if f(i) == a:
        print(i)
        break
else:
    print(-1)



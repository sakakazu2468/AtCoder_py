n = int(input())
x = input()

def popcount(x):
    global count
    if x==0:
        return
    else:
        count += 1
        x_b = bin(x)
        popcount(x % x_b.count('1'))

lx = len(x)
for i in range(lx):
    if x[i]=='1':
        bin_num = int(x, 2)-2**(lx-1-i)
    else:
        bin_num = int(x, 2)+2**(lx-1-i)

    count = 0
    popcount(bin_num)
    print(count)

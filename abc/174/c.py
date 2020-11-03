k = int(input())
if k%2==0:
    print(-1)
else:
    count = 1
    num = 7
    for i in range(10**6):
        if num%k==0:
            print(count)
            break
        else:
            count += 1
            num = num*10 + 7
    else:
        print(-1)

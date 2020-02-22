n = int(input())
a = list(map(int, input().split()))

for i in a:
    if not i%2:
        if i%3==0 or i%5==0:
            pass
        else:
            print("DENIED")
            break
else:
    print("APPROVED")

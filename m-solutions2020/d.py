n = int(input())
a = list(map(int, input().split()))
money = 1000
trade = False
num = 0
while num != len(a)-1:
    if a[num] == a[num+1]:
        a.remove(a[num])
    else:
        num += 1
for i in range(len(a)):
    if i == 0:
        a1 = a[i]
        a2 = a[i+1]
        if a1 < a2:
            count = money//a1
            money = money%a1
            trade = True
    elif 0 < i < len(a)-1:
        a1 = a[i-1]
        a2 = a[i]
        a3 = a[i+1]
        if ((a1 > a2) and (a3 > a2) and (trade==False)):
            count = money//a2
            money = money%a2
            trade = True
        elif ((a1 < a2) and (a3 < a2) and (trade==True)):
            money += a2*count
            trade = False
    else:
        if trade:
            if len(a) < 3:
                money += a2*count
            else:
                money += a3*count


print(money)


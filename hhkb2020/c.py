n = int(input())
p = list(map(int, input().split()))
num = [0 for i in range(200000+10)]
mini = 0
for i in p:
    num[i] = 1
    if num[mini] == 1:
        while True:
            mini += 1
            if num[mini] == 0:
                break
    print(mini)
hw1 = list(map(int, input().split()))
hw2 = list(map(int, input().split()))
for i in range(2):
    if hw1[i] in hw2:
        print("YES")
        break
else:
    print("NO")

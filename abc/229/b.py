a, b = input().split()
for i in range(min(len(a), len(b))):
    if int(a[-1*(i+1)]) + int(b[-1*(i+1)]) >= 10:
        print("Hard")
        break
else:
    print("Easy")

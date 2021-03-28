x = input()
for i in range(len(x)):
    if x[-1*(i+1)]==".":
        point = -1*(i+1)
        break
else:
    point = 0
if point == 0:
    print(int(x))
else:
    print(int(x[:point]))


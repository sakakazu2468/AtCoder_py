n = input()
zero = 0
for i in range(len(n)):
    idx = -1*(i+1)
    if n[idx] == "0":
        zero += 1
    else:
        break
n = "0"*zero + n
for i in range(len(n)//2):
    back_idx = -1*(i+1)
    if n[i] != n[back_idx]:
        print("No")
        break
else:
    print("Yes")



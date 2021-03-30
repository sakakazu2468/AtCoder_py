n = int(input())
s = input()
left = 0
right = 0
for i in range(n):
    if s[i]=="(":
        left += 1
    else:
        if left==0:
            right += 1
        else:
            left -= 1
print("("*right + s + ")"*left)

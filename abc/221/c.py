n = list(input()[:])
n.sort(reverse=True)

n1 = n[0]
n2 = n[1]

for i in range(2, len(n)):
    n1d = n1+n[i]
    n2d = n2+n[i]
    if int(n1d)*int(n2) > int(n1)*int(n2d):
        n1 += n[i]
    else:
        n2 += n[i]

print(int(n1)*int(n2))

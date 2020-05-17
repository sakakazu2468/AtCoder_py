o = input()
e = input()
oi = 0
ei = 0
s = ""
for i in range(len(o)+len(e)):
    if i%2==0:
        s += o[oi]
        oi += 1
    else:
        s += e[ei]
        ei += 1
print(s)

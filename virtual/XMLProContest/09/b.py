o = input()
e = input()
pas = ""
for i in range(len(e)):
    pas += o[i]
    pas += e[i]
if len(o) != len(e):
    pas += o[-1]
print(pas)

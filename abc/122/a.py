b = input()
at = ['A', 'T']
cg = ['C', 'G']
if b in at:
    at.remove(b)
    print(at[0])
else:
    cg.remove(b)
    print(cg[0])

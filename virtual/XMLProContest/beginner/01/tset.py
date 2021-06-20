m = []
# N = int(input("ドーナツの数"))
N, X = list(map(int, input().split()))

i = 0
flag = 0
while i != N:
    v= int(input())
    m.append(v)
    i+=1
moto = X - sum(m)
kosu = moto//min(m)
print(kosu + len(m))

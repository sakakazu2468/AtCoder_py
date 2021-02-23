n, c = map(int, input().split())
odd = [0 for _ in range(10)]
even = [0 for _ in range(10)]
for i in range(n):
    a = int(input())
    if i%2 == 0:
        even[a-1] += 1
    else:
        odd[a-1] += 1
e_max1 = max(even)
e_max1_idx = even.index(e_max1)
even[e_max1_idx] = 0
e_max2 = max(even)

o_max1 = max(odd)
o_max1_idx = odd.index(o_max1)
odd[o_max1_idx] = 0
o_max2 = max(odd)

if e_max1_idx!=o_max1_idx:
    print((n-e_max1-o_max1)*c)
else:
    eo = (n-e_max1-o_max2)*c
    oe = (n-o_max1-e_max2)*c
    print(min(eo, oe))


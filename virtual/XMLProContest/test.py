import copy


n, m, l = map(int, input().split())
p, q, r = map(int, input().split())
pack = [p, q, r]


def rem(i, j):
    pack_c = copy.deepcopy(pack)
    pack_c.remove(i)
    pack_c.remove(j)
    return pack_c[0]


ans = -1
for i in range(len(pack)):
    for j in range(len(pack)):
        if i==j:
            continue
        n_div = n//pack[i]
        m_div = m//pack[j]
        l_div = l//rem(pack[i], pack[j])
        ans = max(n_div*m_div*l_div, ans)
print(ans)


n, k = map(int, input().split())
a = []
a_sort = []
for i in range(n):
    in_a = list(map(int, input().split()))
    a.append(in_a)
    a_sort += in_a

rank = {}
for i in range(len(a_sort)):
    rank[a_sort[i]] = rank.get(a_sort[i], i)


k_range = []
for i in range(k):
    k_range.append(a[i][:k])
print(k_range)

rank_a = [0 for i in range(n**2)]


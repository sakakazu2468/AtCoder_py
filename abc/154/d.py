n, k = map(int, input().split())
p = list(map(int, input().split()))
m = []
m_sum = 0
for i in range(n-k+1):
    if i == 0:
        p_sum = sum(p[:k])
    else:
        p_sum -= p[i-1]
        p_sum += p[i+k-1]
    if p_sum > m_sum:
        m_sum = p_sum
print((m_sum+k)/2)


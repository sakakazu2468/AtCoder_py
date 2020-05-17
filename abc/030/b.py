n, m = map(int, input().split())
m_ang = m * 6
n_ang = (n%12)*5*6 + m*0.5
print(min(abs(m_ang-n_ang), 360-abs(m_ang-n_ang)))

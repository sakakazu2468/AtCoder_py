n, m = map(int, input().split())
room = [0 for i in range(n+10)]
st = []
for i in range(m):
    s, t = map(int, input().split())
    room[s] += 1
    room[t+1] -= 1
    st.append([s, t])

one_room = [0 for i in range(n+10)]
for i in range(1, len(room)):
    room[i] += room[i-1]
    if room[i] < 2:
        one_room[i] = 1

for i in range(1, len(one_room)):
    one_room[i] += one_room[i-1]

ans = []
for i in range(len(st)):
    if (one_room[st[i][1]]-one_room[st[i][0]-1]) == 0:
        ans.append(i+1)

print(len(ans))
for i in ans:
    print(i)


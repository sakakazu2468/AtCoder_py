n = int(input())
music = []
for i in range(n):
    s, t = input().split()
    t = int(t)
    music.append([s, t])
x = input()

ans = 0
time = False
for i in range(n):
    if time:
        ans += music[i][1]
    if music[i][0] == x:
        time = True

print(ans)

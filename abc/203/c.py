n, k = map(int, input().split())
friends = []
for i in range(n):
    a, b = map(int, input().split())
    friends.append([a, b])

friends.sort()

state = 0
for i in range(n):
    if k-(friends[i][0]-state) < 0:
        print(state+k)
        break
    else:
        k -= friends[i][0]-state
        state = friends[i][0]
        k += friends[i][1]
else:
    print(state+k)


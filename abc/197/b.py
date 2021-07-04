h, w, y, x = map(int, input().split())
grid = []
for i in range(h):
    grid.append(input())

x -= 1
y -= 1
ans = 1
x_minus = x
while True:
    x_minus -= 1
    if x_minus < 0:
        break
    if grid[y][x_minus] == ".":
        ans += 1
    else:
        break
x_plus = x
while True:
    x_plus += 1
    if x_plus > w-1:
        break
    if grid[y][x_plus] == ".":
        ans += 1
    else:
        break
y_minus = y
while True:
    y_minus -= 1
    if y_minus < 0:
        break
    if grid[y_minus][x] == ".":
        ans += 1
    else:
        break
y_plus = y
while True:
    y_plus += 1
    if y_plus > h-1:
        break
    if grid[y_plus][x] == ".":
        ans += 1
    else:
        break

print(ans)

x_1, y_1, x_2, y_2 = map(int, input().split())
d_x = x_2-x_1
d_y = y_2-y_1
print(x_2-d_y, y_2+d_x, x_1-d_y, y_1+d_x)

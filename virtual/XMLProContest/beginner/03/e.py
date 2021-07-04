n = int(input())
housex = []
housey = []
for i in range(n):
    x, y = map(int, input().split())
    housex.append([x, i])
    housey.append([y, i])

housex.sort()
housey.sort()


max_list = []
max_list.append([housex[-1][0]-housex[0][0], sorted([housex[-1][1], housex[0][1]])])
max_list.append([housex[-2][0]-housex[0][0], sorted([housex[-2][1], housex[0][1]])])
max_list.append([housex[-1][0]-housex[1][0], sorted([housex[-1][1], housex[1][1]])])
max_list.append([housey[-1][0]-housey[0][0], sorted([housey[-1][1], housey[0][1]])])
max_list.append([housey[-2][0]-housey[0][0], sorted([housey[-2][1], housey[0][1]])])
max_list.append([housey[-1][0]-housey[1][0], sorted([housey[-1][1], housey[1][1]])])

max_list.sort()
max_num = max_list[-1][1]
max_list = max_list[:-1]
for i in range(5):
    if max_list[-1*(i+1)][1] != max_num:
        print(max_list[-1*(i+1)][0])
        break

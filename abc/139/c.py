n = int(input())
h = list(map(int, input().split()))
count = 0
max_list = []
for i in range(len(h)-1):
    if h[i] >= h[i+1]:
        count += 1
        if i == len(h)-2:
            max_list.append(count)
    else:
        max_list.append(count)
        count = 0
if n == 1:
    print(0)
else:        
    print(max(max_list))
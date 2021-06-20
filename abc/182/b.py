n = int(input())
a = list(map(int, input().split()))
ans_list = [0 for i in range(1010)]
for i in range(2, 1001):
    for j in range(n):
        if a[j]%i==0:
            ans_list[i] += 1

print(ans_list.index(max(ans_list)))
        



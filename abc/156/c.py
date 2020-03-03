n = int(input())
x = list(map(int, input().split()))
m = max(x)
ans = [] 
for i in range(101):
    sum_dis = 0
    for j in range(len(x)):
        sum_dis += (x[j]-i)**2
    ans.append(sum_dis)
print(min(ans))
    

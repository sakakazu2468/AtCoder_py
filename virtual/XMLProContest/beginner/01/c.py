k = int(input())
abc_max = 2*10**5 +100
ans = 0
for i in range(1, abc_max+10):
    for j in range(1, abc_max//i+10):
        ans += k//(i*j)
print(ans)

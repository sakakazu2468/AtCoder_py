n = int(input())
a = list(map(int, input().split()))
jyunban = [0 for i in range(n)]
for i in range(n):
    jyunban[a[i]-1] += i+1
for i in range(n):
    print(jyunban[i], end = " ")
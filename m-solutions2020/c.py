n, k = map(int, input().split())
a = list(map(int, input().split()))
score = 1
for i in range(n):
    if i < k:
        score *= a[i]
    else:
        pre = score
        score = score//a[i-k]*a[i]
        if score > pre:
            print("Yes")
        else:
            print("No")


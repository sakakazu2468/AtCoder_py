n, k = map(int, input().split())
rem = n%k
print(min(rem, abs(rem-k)))

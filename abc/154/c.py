n = int(input())
a = list(map(int, input().split()))
set_a = set(a)
if len(a) == len(set_a):
    print("YES")
else:
    print("NO")

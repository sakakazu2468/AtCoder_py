t = int(input())
for i in range(t):
    l, r = map(int, input().split())
    kosuu = r-l-l+1
    kosuu = max(0, kosuu)
    print(kosuu*(kosuu+1)//2)

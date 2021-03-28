n = input()
if len(n)%2 == 0:
    half_n = n[:len(n)//2]
    half_n = int(half_n)
    ans = 0
    for i in range(len(str(half_n))-1):
        ans += 9*(10**i)
    ans += half_n - ((10**(len(str(half_n))-1))-1)
    if half_n > int(n[len(n)//2:]):
        ans -= 1
    print(ans)
else:
    print(0)

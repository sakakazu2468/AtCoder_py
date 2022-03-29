n = int(input())
ans = "AGC"
if n >= 42:
    print(ans+"0"*(3-len(str(n+1)))+str(n+1))
else:
    print(ans+"0"*(3-len(str(n)))+str(n))

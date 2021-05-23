t, n = map(int, input().split())
tmp = n/(t/100)
tmp_int = int(tmp)
if tmp == tmp_int:
    print(tmp_int+n-1)
else:
    print(tmp_int+n)

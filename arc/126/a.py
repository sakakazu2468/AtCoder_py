t = int(input())
for i in range(t):
    ans = 0
    n2, n3, n4 = map(int, input().split())
    n3 = n3//2
    n4use = n4-n3
    if n4use < 0:
        ans += n4
        n2use = n2+n4use*2
        if n2use < 0:
            ans += n2//2
        else:
            ans += -1*n4use
            ans += n2//5
    else:
        ans += n3
        if n4use%2 == 0:
            n2use = n2-n4use//2
            if n2use < 0:
                ans += n2
            else:
                ans += n4use//2
                ans += n2use//5
        else:
            n2use = n2-n4use//2
            if n2use < 0:
                ans += n2
            else:
                ans += n4use//2
                n2use -= 3
                ans += 1
                ans += n2use//5
    print(ans)

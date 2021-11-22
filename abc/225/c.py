n, m = map(int, input().split())
prevs = []

def check(prev, nxt):
    prev %= 7
    nxt %= 7
    if prev+1 == nxt:
        return True
    elif prev == 6 and nxt == 0:
        return True
    else:
        return False


for i in range(n):
    b = list(map(lambda x:int(x)-1, input().split()))
    if i==0:
        for j in range(m):
            if j != 0:
                if prevs[-1]%7+1 != b[j]%7 or prevs[-1]+1 != b[j]:
                    print("No")
                    break
            prevs.append(b[j])
        else:
            continue
        break
    else:
        for j in range(m):
            if b[j] == prevs[j]+7:
                prevs[j] += 7
            else:
                print("No")
                break
        else:
            continue
        break
else:
    print("Yes")

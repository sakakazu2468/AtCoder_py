n = int(input())
s = input()
for i in range(100):
    if i == 0:
        ac = 'b'
    elif i%3 == 0:
        ac = 'b' + ac + 'b'
    elif i%3 == 1:
        ac = 'a' + ac + 'c'
    else:
        ac = 'c' + ac + 'a'

    if len(s) == len(ac):
        if s == ac:
            print(i)
            break
        else:
            print(-1)
            break
    elif len(s) < len(ac):
        print(-1)
        break


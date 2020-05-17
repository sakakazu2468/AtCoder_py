a = input()
b = input()
c = input()
card = a[0]
a = a[1:]
while True:
    if card == "a":
        if a == "":
            print('A')
            break
        card = a[0]
        a = a[1:]
    elif card == "b":
        if b == "":
            print('B')
            break
        card = b[0]
        b = b[1:]
    else:
        if c == "":
            print('C')
            break
        card = c[0]
       c = c[1:]

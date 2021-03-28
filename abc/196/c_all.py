n = input()
if len(n) == 1:
    print(0)
else:
    if len(n)%2 != 0:
        n = "9"*(len(n)-1)
    head = n[:len(n)//2]
    tail = n[len(n)//2:]
    if int(head) > int(tail):
        print(int(head)-1)
    else:
        print(int(head))

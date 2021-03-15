a, b, w = map(int, input().split())
w_g = w*1000
if 33>=(b-a):
    print("UNSATISFIABLE")
else:
    a_num = w_g//a
    b_num = w_g//b
    if w_g%b!=0:
        b_num += 1

    print(b_num, a_num)

s = input()
if s[0] != "A":
    print("WA")
else:
    c_count = 0
    for i in range(2, len(s)-1):
        if s[i] == "C":
            c_count += 1
    if c_count == 1:
        upper = 0
        lower = 0
        for i in s:
            if 97 <= ord(i) <= 122:
                lower += 1
            else:
                upper += 1
        if upper == 2:
            print("AC")
        else:
            print("WA")
        # if upper != 2:
        #     print("WA")
        # else: 
        #     print("AC")
    else:
        print("WA")


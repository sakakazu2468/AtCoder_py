from itertools import permutations


s1 = list(input())[:]
s2 = list(input())[:]
s3 = list(input())[:]
chr_union = set(s1) | set(s2) | set(s3)
if len(chr_union) > 10:
    print("UNSOLVABLE")
else:
    chr_list = list(chr_union)
    numbers = [f"{i}" for i in range(10)]
    for number_set in list(permutations(numbers, len(chr_union))):
        n1 = ""
        n2 = ""
        n3 = ""
        for ch in s1:
            n1 += number_set[chr_list.index(ch)]
        for ch in s2:
            n2 += number_set[chr_list.index(ch)]
        for ch in s3:
            n3 += number_set[chr_list.index(ch)]
        if int(n1) + int(n2) == int(n3):
            if n1[0] != "0" and n2[0] != "0" and n3[0] != "0":
                print(n1)
                print(n2)
                print(n3)
                break
    else:
        print("UNSOLVABLE")

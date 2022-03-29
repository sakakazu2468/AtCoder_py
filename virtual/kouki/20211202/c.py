n = int(input())
words_n = set()
words_e = set()
for i in range(n):
    s = input()
    if s[0] == "!":
        words_e.add(s[1:])
    else:
        words_n.add(s)
en = len(words_e)
nn = len(words_n)
words_en = words_n | words_e
if en+nn == len(words_en):
    print("satisfiable")
else:
    print(list(words_e & words_n)[0])

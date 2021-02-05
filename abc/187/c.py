n = int(input())
words = set()
for i in range(n):
    words.add(input())
total = len(words)
words = list(words)

test_words = set()
for i in range(total):
    length = len(test_words)
    ipt = words[i]
    if ipt[0] == '!':
        ipt = ipt[1:]
    test_words.add(ipt)
    add_length = len(test_words)
    if length == add_length:
        print(ipt)
        break
else:
    print("satisfiable")

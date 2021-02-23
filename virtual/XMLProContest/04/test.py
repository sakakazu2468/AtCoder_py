import functools
import itertools

n = int(input())
wordhead = {}
for i in range(n):
    s = input()
    wordhead[s[0]] = wordhead.get(s[0], 0) + 1

ans = 0
for chars in itertools.combinations("MARCH", 3):
    value = []
    for char in chars:
        value.append(wordhead.get(char, 0))
    # value = list(map(lambda x: wordhead.get(x, 0), chars))
    ans += functools.reduce(lambda mult1, mult2: mult1 * mult2, value)
print(ans)


n = int(input())
original = []
sorting = []
for i in range(n):
    word = input()
    original.append(word)
    reverse_word = ""
    for j in range(len(word)):
        reverse_word += word[len(word)-j-1]
    sorting.append([reverse_word, i])
sorting.sort()
for i in range(n):
    print(original[sorting[i][1]])
    

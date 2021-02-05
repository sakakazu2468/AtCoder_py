l = int(input())
child = 1
l -= 1
for i in range(11):
    child *= l-i
mother = 1
for i in range(11):
    mother *= i+1
print(child//mother)

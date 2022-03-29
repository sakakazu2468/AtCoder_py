import random

a = random.randint(1, 12)
while True:
    b = random.randint(1, 12)
    if a <= b:
        break
print(a, b)

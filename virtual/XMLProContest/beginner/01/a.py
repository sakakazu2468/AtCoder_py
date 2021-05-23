h, m = map(int, input().split())

minits = 0
if m != 0:
    minits += 60 - m
    h += 1
minits += (18 - h) * 60

print(minits)

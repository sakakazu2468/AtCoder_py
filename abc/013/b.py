a = int(input())
b = int(input())
print(min(max(a, b)-min(a, b), int('1'+str(min(a, b)))-max(a, b)))

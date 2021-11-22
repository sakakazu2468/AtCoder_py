n, x = map(int, input().split())
a = list(map(lambda y: int(y)-1, input().split()))
tf = [False for _ in range(n)]
x -= 1
sec = x
while True:
    if tf[sec] == True:
        break
    tf[sec] = True
    sec = a[sec]
    
print(sum(tf)) 

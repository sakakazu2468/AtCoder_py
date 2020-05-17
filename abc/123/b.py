a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
ans = 0
plus = 0
while plus < a:
    plus += 10
ans += plus

plus = 0
while plus < b:
    plus += 10
ans += plus

plus = 0
while plus < c:
    plus += 10
ans += plus

plus = 0
while plus < d:
    plus += 10
ans += plus

plus = 0
while plus < e:
    plus += 10
ans += plus

minus = [int(str(a)[-1]), int(str(b)[-1]), int(str(c)[-1]), int(str(d)[-1]), int(str(e)[-1])]
minus.sort()
for i in minus:
    if i !=0:
        ans -= 10-i
        break
print(ans)

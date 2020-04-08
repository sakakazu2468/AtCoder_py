n = int(input())
h = n//3600
n -= h*3600
m = n//60
n -= m*60
print("{:02}:{:02}:{:02}".format(h, m, n))

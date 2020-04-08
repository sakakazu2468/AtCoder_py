a, b = map(int, input().split())

def gcd(a, b):
    if a == 0:
        return 
    a, b = a%b, a
    gcd(a, b)

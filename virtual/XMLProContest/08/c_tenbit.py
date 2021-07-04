n = int(input())
count = 0
bound = 0
i = 1
half = n // 2
right = n + 1
while True:
  bound = (half * (half + 1)) / 2
  if bound > n+1:
    right = half
    half = right // 2
  else:
    if bound + half + 1 > n + 1:
      break
    half = (half + right) // 2
print(n+1 - half)

b, c = map(int, input().split())
minus_continue = b - c//2
if c%2==0:
    mult_minus = (minus_continue+1)*-1
else:
    mult_minus = minus_continue*-1
first_mult = b*-1
rem = c-1
minus_mult = first_mult - rem//2
if rem%2==0:
    minus_minus = (minus_mult+1)*-1
else:
    minus_minus = minus_mult*-1
rng1 = [max(minus_minus, b), minus_continue]
rng2 = [minus_mult, mult_minus]
if (max(rng1) >= max(rng2)) and (min(rng1) <= min(rng2)):
    print(max(rng1)-min(rng1)+1)
elif (max(rng2) >= max(rng1)) and (min(rng2) <= min(rng1)):
    print(max(rng2)-min(rng2)+1)
elif max(max(rng1), max(rng2)) == max(rng1):
    if min(rng1) > max(rng2):
        print(max(rng1)-min(rng1)+1 + max(rng2)-min(rng2)+1)
    else:
        print(max(rng1)-min(rng2)+1)
else:
    if max(rng1) < min(rng2):
        print(max(rng1)-min(rng1)+1 + max(rng2)-min(rng2)+1)
    else:
        print(max(rng2)-min(rng1)+1)


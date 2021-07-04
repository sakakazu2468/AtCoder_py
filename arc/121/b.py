n = int(input())
rdog = []
gdog = []
bdog = []
colors = [0, 0, 0]
for i in range(n*2):
    a, c = input().split()
    if c=="R":
        colors[0] += 1
        rdog.append(int(a))
    elif c=="G":
        colors[1] += 1
        gdog.append(int(a))
    else:
        colors[2] += 1
        bdog.append(int(a))

rdog.sort()
gdog.sort()
bdog.sort()
dogs = [rdog, gdog, bdog]

if colors[0]%2 + colors[1]%2 + colors[2]%2 == 0:
    print(0)
else:
    odd = []
    for i in range(3):
        if colors[i]%2 != 0:
            odd.append(i)
    even = [0, 1, 2]
    even.remove(odd[0])
    even.remove(odd[1])
    even = even[0]

    ii = 0
    jj = 0
    mdiff = 10**16
    while True:
        if not (len(dogs[odd[0]]) and len(dogs[odd[1]])):
            break
        numi = dogs[odd[0]][0]
        numj = dogs[odd[1]][0]
        mdiff = min(abs(numj-numi), mdiff)
        if (ii == len(dogs[odd[0]])-1) and (jj == len(dogs[odd[1]])-1):
            break
        elif numi == len(dogs[odd[0]])-1:
            jj += 1
        elif numi == len(dogs[odd[1]])-1:
            ii += 1
        elif numi < numj:
            ii += 1
        elif numi > numj:
            jj += 1
        else:
            ii += 1
    ii = 0
    jj = 0
    eodiff = 10**16
    while True:
        if not (len(dogs[even]) and len(dogs[odd[1]])):
            break
        numi = dogs[even][0]
        numj = dogs[odd[1]][0]
        eodiff = min(abs(numj-numi), eodiff)
        if (ii == len(dogs[even])-1) and (jj == len(dogs[odd[1]])-1):
            break
        elif numi == len(dogs[even])-1:
            jj += 1
        elif numi == len(dogs[odd[1]])-1:
            ii += 1
        elif numi < numj:
            ii += 1
        elif numi > numj:
            jj += 1
        else:
            ii += 1
    ii = 0
    jj = 0
    oediff = 10**16
    while True:
        if not (len(dogs[odd[0]]) and len(dogs[even])):
            break
        numi = dogs[odd[0]][0]
        numj = dogs[even][0]
        oediff = min(abs(numj-numi), oediff)
        if (ii == len(dogs[odd[0]])-1) and (jj == len(dogs[even])-1):
            break
        elif numi == len(dogs[odd[0]])-1:
            jj += 1
        elif numi == len(dogs[even])-1:
            ii += 1
        elif numi < numj:
            ii += 1
        elif numi > numj:
            jj += 1
        else:
            ii += 1

    print(min(mdiff, eodiff+oediff))

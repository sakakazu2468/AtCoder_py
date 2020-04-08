k = int(input())

def lunlun(rank, keta, count):
    global k
    if count < k-9:
        return 
    keta -= 1
    if keta == 0:

    for i in range(len(rank)):
        if rank[i] == '0':
            return lunlun(['0', '1'], keta, count+1)
        elif rank[i] == 9:
            return lunlun(['8', '9'], keta, count+1)
        else:
            return lunlun([str(int(rank)-1), rank, str(int(rank)+1)], keta, count+1)

if k < 10:
    print(k)
else:
    lun_num = ['1', '0']
    keta = 1
    i = 0
    while i < k-9:
        ret = lunlun(keta-1)
        for j in range(len(ret)):
            lun_num[keta] = ret[j] 
            i += 1
            if i == k-9:
                break
        lun_num[keta] = lunlun(keta-1) 

        if lun_num[0] == '9':
            keta += 1
            lun_num = ['1'] + ['0' for i in range(keta)]


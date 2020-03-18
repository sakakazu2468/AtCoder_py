import heapq


n = int(input())
tree = [[] for i in range(n+1)]
dep_table = [[] for i in range(n+1)]
dep_table[0].append(1)
depth = 1 
for i in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
    
    if not a in dep_table[depth-1]:
        depth += 1
    dep_table[depth].append(b)

order = [[] for i in range(n+1)]
depth_num = 0
for i in range(len(dep_table)):
    for j in dep_table[i]:
        if depth_num == depth:
            break

        if depth_num==depth-2 and depth_num==depth-1:
            not_under = list(set(dep_table[depth_num+1])-set(tree[j]))
            order[j] = not_under
        else:
            not_under = list(set(dep_table[depth_num+1])-set(tree[j]))
            order[j] = dep_table[depth_num+3]+not_under
    else:
        depth_num += 1

mult3 = n//3
if n%3 == 2:
    plus1 = n//3+1
    plus2 = n//3+1
else:
    plus1 = n//3+1
    plus2 = n//3

ord_len = []
ans_list = [0 for i in range(n+1)]


def insert_2():
    global ans_list, plus1, plus2
    poped = heapq.heappop(ord_len)
    ans_list[poped[1]] = 2
    plus2 -= 1
    for i in range(poped[0]):
        comb = order[poped[1]][i]
        if ans_list[comb] == 0:
            if plus1 == 0:
                return -1
            ans_list[comb] = 1
            plus1 -= 1
        elif ans_list[comb] == 1:
            pass
        else:
            return -1

def insert_1():
    global ans_list, plus1, plus2
    poped = heapq.heappop(ord_len)
    ans_list[poped[1]] = 1
    plus1 -= 1
    for i in range(poped[0]):
        comb = order[poped[1]][i]
        if ans_list[comb] == 0:
            if plus2 == 0:
                return -1
            ans_list[comb] = 2
            plus2 -= 1
        elif ans_list[comb] == 2:
            pass
        else:
            return -1

for i in range(len(order)):
    heapq.heappush(ord_len, [-1*len(order[i]), i])
while mult3 != 0 and ord_len[0] != 0:
    ans_list[heapq.heappop(ord_len)[1]] = 3
    mult3 -= 1
else:
    if ord_len[0] == 0:
        pass
    else:
        while ord_len[0][0] != 0:
            if plus1 == 0:
                if insert_2() == -1:
                    print(-1)
                    break
            elif plus2 == 0:
                if insert_1() == -1:
                    print(-1)
                    break
            elif plus1 > plus2:
                if insert_2() == -1:
                    print(-1)
                    break
            else:
                if insert_1() == -1:
                    print(-1)
                    break
        else:                           # 条件の対象のみ順列が完成 
            for i in range(1, n+1):
                if ans_list[i] == 0:
                    if mult3 != 0:
                        ans_list[i] = 3
                        mult3 -= 1
                    elif plus1 != 0:
                        ans_list[i] = 1
                        plus1 -= 1
                    elif plus2 != 0:
                        ans_list[i] = 2
                        plus2 -= 1

            count1 = 0
            count2 = 0
            count3 = 0
            for i in range(1, n+1):
                if ans_list[i] == 1:
                    ans_list[i] = 3*count1+1
                    count1 += 1
                elif ans_list[i] == 2:
                    ans_list[i] = 3*count2+2
                    count2 += 1
                elif ans_list[i] == 3:
                    ans_list[i] = 3*count3+3
                    count3 += 1
            for i in range(1, n+1):
                if i==n:
                    print(ans_list[i])
                else:
                    print(ans_list[i], end="")

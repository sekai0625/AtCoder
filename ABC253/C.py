q = int(input())

l = []
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        l.append(query[1])
    elif query[0] == 2:
        d_num = query[2]
        result = [i for i in l if i == query[1]]
        if query[2] > len(result):
            d_num = len(result)
        
        for _ in range(d_num):
            l.remove(query[1])
    elif query[0] == 3:
        print(max(l) - min(l))



q = int(input())

l = []
for _ in range(q):
    a, b, c = map(int, input().split())
    if a == 1:
        l.append(b)
    elif a == 2:
        d_num = c
        result = [i for i in l if i == b]
        if c > len(result):
            d_num = len(result)
        
        for _ in range(d_num):
            l.remove(b)
    elif a == 3:
        print(l)



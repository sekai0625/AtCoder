n, q = map(int, input().split())
x = list(int(input()) - 1 for i in range(q))    #ボールに書かれた整数は0~n-1

val = list(range(n)) #val[i]:i番目のボールに書かれた整数
pos = list(range(n)) #pos[i]:整数iが書かれたボールの位置
for i in x:
    p = pos[i]
    if p < n - 1:
        v = val[p + 1]
        val[p], val[p + 1] = val[p + 1], val[p]
        pos[i] += 1
        pos[v] -= 1
    else:
        v = val[p - 1]
        val[p - 1], val[p] = val[p], val[p - 1]
        pos[i] -= 1
        pos[v] += 1

for i in val:
    print(i + 1, end=" ")

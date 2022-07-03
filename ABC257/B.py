n, k, q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))

field = [0 for _ in range(n)]
num = 1
for a in A:
    field[a - 1] = num
    num += 1

for l in L:
    for i in range(n):
        if field[i] == l:
            if i == n - 1:
                continue
            elif field[i + 1] == 0:
                field[i + 1] = l
                field[i] = 0
            
# print(field)
result = [field.index(f) + 1 for f in field if f != 0]
print(*result) # 空白出力
import itertools # 全ての組み合わせ

n, w = map(int, input().split())
A = list(map(int, input().split()))

A2 = []
for pair in itertools.combinations(A, 2): 
    A2.append(sum(pair))

for pair in itertools.combinations(A, 3):
    A2.append(sum(pair))

cnt = 0
A += A2
A = list(set(A))
for a in A: # set()：重複除去
    if a <= w:
        cnt += 1

# print(A)
print(cnt)
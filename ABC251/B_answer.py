n, w = map(int, input().split())
A = list(map(int, input().split()))

A2 = []
for i in range(n):
    for j in range(i + 1, n):
        A2.append(A[i] + A[j])

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            A2.append(A[i] + A[j] + A[k]) 


cnt = 0
A += A2
A = list(set(A))
for a in A: # set()：重複除去
    if a <= w:
        cnt += 1

# print(A)
print(cnt)
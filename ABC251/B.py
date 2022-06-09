import itertools 

n, w = map(int, input().split())
A = list(map(int, input().split()))

for i in range(n):
    j = i + 1
    while j < n:
        A.append(A[i] + A[j])
        j += 1

for i in range(n):
    j = i + 1
    while j + 1 < n:
        A.append(A[i] + A[j] + A[j + 1])
        j += 1

cnt = 0
for a in set(A): # set()：重複除去
    if a <= w:
        cnt += 1

print(A)
print(cnt)
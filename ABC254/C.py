import random

n, k = map(int, input().split(' '))

A = [random.randint(1, 10^9) for _ in range(n)]
sorted_A = A
sorted_A.sort()
for i in range(n + 1):
    if i + k <= n:
        if A[i] > A[i + k]:
            A[i], A[i + k] = A[i + k], A[i]

flag = 0
for i in range(n + 1):
    if i + k <= n:
        if A[i] != sorted_A[i]:
            flag = 1

if flag == 0:
    print('Yes')
else:
    print('No')
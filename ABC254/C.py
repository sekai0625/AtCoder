import copy

n, k = map(int, input().split(' '))

A = list(map(int, input().split(' ')))
sorted_A = copy.copy(A)
sorted_A.sort()
for i in range(n):
    if i + k < n:
        if A[i] > A[i + k]:
            A[i], A[i + k] = A[i + k], A[i]

flag = 0
for i in range(n):
    if A[i] != sorted_A[i]:
            flag = 1

# print("{}\n{}".format(sorted_A, A))

if flag == 0:
    print('Yes')
else:
    print('No')
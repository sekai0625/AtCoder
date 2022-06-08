n, k = map(int, input().split(' '))
A = list(map(int, input().split(' ')))
B = list(map(int, input().split(' ')))

A_max = max(A)

flag = 0
for b in B:
    if A[b - 1] == A_max:
        flag = 1
        break

if flag == 1:
    print('Yes')
else:
    print('No')
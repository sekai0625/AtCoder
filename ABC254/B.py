n = int(input())

A = []
for i in range(n):
    tmp = []
    for j in range(i + 1):
        if j == 0 or i == j:
            tmp.append(1)
        else:
            A_tmp = A[i-1]
            tmp.append(A_tmp[j-1] + A_tmp[j])
    A.append(tmp)

for a in A:
    a = list(map(str, a))
    line = ' '.join(a)
    print(line)

from turtle import back

from numpy import append


N, A, B = map(int, input().split())

tile = [['.'] * N * B for _ in range(N * A)]

for i in range(N):
    if i % 2 == 0:
        for j in range(N):
            if j % 2 != 0:
                for a in range(A):
                    for b in range(B):
                        tile[i * A + a][j * B + b] = '#'
    else:
        for j in range(N):
            if j % 2 == 0:
                for a in range(A):
                    for b in range(B):
                        tile[i * A + a][j * B + b] = '#'

for i in range(N * A):
    print("".join(tile[i]))
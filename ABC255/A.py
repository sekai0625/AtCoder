r, c = map(int, input().split())
A = []
for _ in range(2):
    A.append(list(map(int, input().split())))

print(A[r - 1][c - 1])
# print(A)
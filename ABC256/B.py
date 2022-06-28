n = int(input())
A = list(map(int, input().split()))
p = 0

# masu = [0 for _ in range(n)]
# for i in range(n):
#     for j in range(i + 1):
#         masu[j] += A[i]

# p = 0
# for i in range(n):
#     if masu[i] > 4:
#         p += 1
# # print(masu)
# print(p)

field = [0, 0, 0, 0]
for x in A:
    next_field = [0, 0, 0, 0]
    field[0] = 1
    for i in range(4):
        if field[i] == 1:
            if i + x >= 4:
                p += 1
            else:
                next_field[i + x] = 1
    field = next_field
print(p)
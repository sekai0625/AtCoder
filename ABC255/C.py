x, a, d, n = map(int, input().split())

S = []
for i in range(1, n + 1):
    S.append(a + (i - 1) * d)

# print(S)

abs_list = []
for s in S:
    abs_list.append(abs(s - x))

# print(abs_list)
index = abs_list.index(min(abs_list))

count = 0

if x >= S[index]:
    count = x - S[index]
else:
    count = S[index] - x

print(count)
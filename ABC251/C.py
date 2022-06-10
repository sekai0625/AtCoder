n = int(input())
p = [list(map(str, input().split())) for _ in range(n)]

point = 0
index = 0
original = []
for i in range(n):
    flag = p[i][0] in original
    if flag == False:
        original.append(p[i][0])
        if point < int(p[i][1]):
            point = int(p[i][1])
            index = i

print(index + 1)
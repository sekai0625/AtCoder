h, w = map(int, input().split())
r, c = map(int, input().split())

count = 0
for i in range(1, h + 1):
    for j in range(1, w + 1):
        if abs(i - r) + abs(j - c) == 1:
            count += 1
print(count)
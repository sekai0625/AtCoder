n, q = map(int, input().split())

ball = [i - 1 for i in range(1, n + 1)]
x = [int(input()) - 1 for _ in range(q)]
index = list(range(n))

for i in x:
    b = ball[i]
    if i < n -1:
        ball[i] -= 1
    
for b in ball:
    print(b, end=" ")
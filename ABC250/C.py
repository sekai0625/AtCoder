n, q = map(int, input().split())

ball = [i for i in range(1, n + 1)]
X = [int(input()) for _ in range(q)]
for x in X:
    index = ball.index(x)
    if index + 1 < n:
        ball[index], ball[index + 1] = ball[index + 1], ball[index]
    else:
        ball[index], ball[index - 1] = ball[index - 1], ball[index]

print(ball)
N = int(input())
S = list(map(int, input()))
W = list(map(int, input().split(' ')))

X = set()
for w in W:
    X.add(w - 1)
    X.add(w + 1)

i = 0
f = [0 for _ in range(len(X))]
for x in X:
    for n in range(N):
        if W[n] < x:
            w = 0
        else:
            w = 1
        if w == S[n]:
            f[i] += 1
    i += 1
print(max(f))

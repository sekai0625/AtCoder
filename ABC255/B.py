# 全ての人について、その人から最も近い『明かりを持った人』までの距離の最大値

import numpy as np
n, k = map(int, input().split())
A = list(map(int, input().split()))
X = []
for _ in range(n):
    X.append(list(map(int, input().split())))

min = -1
R = []
for a in A:
    max = -1
    for x in X:
        r = np.linalg.norm(np.array(X[a - 1]) - np.array(x))
        if r > max:
            max = r
    R.append(max)

print(np.min(R))
# print(X)
# 全ての人について、その人から最も近い『明かりを持った人』までの距離の最大値

import numpy as np
n, k = map(int, input().split())
A = list(map(int, input().split()))
X = []
for _ in range(n):
    X.append(list(map(int, input().split())))

R = []
for x in X:
    D = []
    for a in A:
        r = np.linalg.norm(np.array(x)- np.array(X[a - 1]))
        D.append(r)
    R.append(np.min(D))

print(np.max(R))
# print(X)
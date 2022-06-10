# TLE する解法

N = int(input())
S, T = [], []
for i in range(N):
    s, t = input().split()
    S.append(s)
    T.append(int(t))

best = -1
best_score = -1

for i in range(N):
    original = True
    for j in range(i):
        if S[i] == S[j]:
            original = False
    if original == False:
        continue
    if best_score < T[i]:
        best = i
        best_score = T[i]

print(best + 1)

# AC する解法

N = int(input())
S, T = [], []
for i in range(N):
    s, t = input().split()
    S.append(s)
    T.append(int(t))

best = -1
best_score = -1

# 集合型は次の操作を O(1) あるいは O(log(集合の要素数)) で行うことができるデータ構造.つまり，高速処理が可能
# ある文字列が集合に含まれているか判定する
# 集合を文字列に追加する

appeared = set() # set:集合を表すデータ型，リストと異なり順番を持たない，重複要素は取り除かれる
for i in range(N):
    if S[i] in appeared:
        continue
    appeared.add(S[i])
    if best_score < T[i]:
        best = i
        best_score = T[i]

print(best + 1)

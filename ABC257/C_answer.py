N = int(input())
S = list(map(int, input()))
W = list(map(int, input().split(' ')))

ans = 0
arr = []
for i in range(N):
    arr.append([S[i], W[i]])
    if S[i] == 1: # すべて大人として捉える
        ans += 1
arr.sort(key=lambda x:x[1]) # sort:元のリストをソート，sorted:ソートした新たなリストを作成
# print(arr)
x = ans
for i in range(N):
    if arr[i][0] == 1: # 1 → 0 にする，つまり，大人から子供に変えた時，元々大人として捉えていたものを子供と間違って捉えているため，-1
        x -= 1
    else:
        x += 1 # 0 → 1 にする，つまり，子供から大人に変えた時，元々大人として捉えていた為正しい判定が出来ているため，+1
    if i < N - 1:
        if arr[i][1] != arr[i + 1][1]:
            ans = max(ans, x)
    else:
        ans = max(ans, x)

print(ans)

n=int(input())
s=[]
for i in range(n):
	s.append(input())

cnt=[[0 for j in range(10)]for i in range(10)]
# 全てのsにおいて，0 ~ 9の数が各々j何番目で何回現れているのか
for i in range(n):
	for j in range(10):
		cnt[int(s[i][j])][j]= cnt[int(s[i][j])][j]+1

mx=[0 for i in range(10)]
for i in range(10):
	for j in range(10):
		mx[i]=max(mx[i], 10 * (cnt[i][j] - 1) + j) # 各番号で揃えようとした場合，最後のボタン(3回目)を押すまでにかかった時間
print(mx)
print(min(mx))
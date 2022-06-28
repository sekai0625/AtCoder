import sys

x, a, d, n = map(int, input().split())
if d == 0:
    print(abs(a - x))
    sys.exit()
m = a + (n - 1) * d  # 末項
ans = min(abs(a - x), abs(m - x))
y = a + (x - a) // d * d
for i in range(-2, 3):  # 周辺 ±2 程度を探索
    z = y + i * d
    if a <= z <= m or m <= z <= a:  # 探索している数が範囲内にあるかどうか
        ans = min(ans, abs(z - x))
print(ans)

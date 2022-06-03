a, b , c = map(int, input().split())
#l = list(a, b ,c)

if (a < b and b < c) or (c < b and b < a):
    print("Yes")
else:
    print("No")
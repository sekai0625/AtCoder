a, b , c = map(int, input().split())
l = [a, b ,c]
l.sort()
center = l[1]

if center == b:
    print("Yes")
else:
    print("No")
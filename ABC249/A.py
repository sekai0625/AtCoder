a, b, c, d, e, f, x = map(int, input().split())

T = 0
A = 0
Tx = x
Ax = x
while Tx > 0:
    if Tx < a:
        a = Tx
    T += a * b    
    Tx -= a
    Tx -= c

while Ax > 0:
    if Ax < d:
        d = Ax
    A += d * e    
    Ax -= d
    Ax -= f


# print("T:{}, A:{}".format(T, A))

if T > A:
    print("Takahashi")
elif T < A:
    print("Aoki")
else:
    print("Draw")
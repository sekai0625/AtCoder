n, a, b = map(int, input().split())

ans = [["."]*(n*b) for _ in range(a*n)]

for i in range(n):
    for j in range(n):
        if (i+j) % 2 == 0:
            continue
        else:
            for ii in range(a*i, a*(i+1)):
                for jj in range(b*j,b*(j+1)):
                    ans[ii][jj]= "#"

for i in ans:
    print("".join(i))
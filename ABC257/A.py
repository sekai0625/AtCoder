n, x = map(int, input().split())

alphabet = [chr(ord("a") + i).upper() for i in range(26)]
# print(alphabet)

string = []
for i in alphabet:
    for j in range(n):
        string.append(i)

print(string[x - 1])
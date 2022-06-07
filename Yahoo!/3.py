import sys


def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    l = []  # (a, b, n)
    for i, v in enumerate(lines):
        if i == 0:
            l = list(map(int, v.split(' ')))

    a = l[0]
    b = l[1]
    n = l[2]

    day = 0
    point = 0
    while point < n:
        point += a

        x = [int(a) for a in str(day)]
        result = 7 in x
        if result:
            point += b

        day += 1

    print(point)
    print(day - 1)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)

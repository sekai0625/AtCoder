import sys


def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    l = []
    kagu = []
    for i, v in enumerate(lines):
        if i == 0:
            l = list(map(int, v.split(' ')))
        else:
            kagu.append(v)

    d = {}
    d2 = {}
    for s in kagu:
        mono = list(s.split(' '))
        d[mono[0]] = int(mono[1])
    # print(kagu)
    d2 = sorted(d.items(), key=lambda x: x[1], reverse=True)

    for i in range(int(l[1])):
        print(d2[i][0])


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)

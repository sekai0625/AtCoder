import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    l = [] # (n, m ,k)
    color = [] # 各地点の色
    road = []
    for i, v in enumerate(lines):
        if i == 0:
            l = list(map(int, v.split(' ')))
        elif i == 1:
            color = list(map(int, v.split(' ')))
        else:
            road.append(list(map(int, v.split(' '))))
    print(road)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)

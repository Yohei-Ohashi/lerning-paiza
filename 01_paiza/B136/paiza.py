import sys


def solve() -> None:  # 型ヒントで値を返さずprintのみを明確化
    # 入力を全て一度に読み込む (paizaとかでよく使われるらしい)
    data = sys.stdin.buffer.read().split()
    it = iter(data)

    N = int(next(it))
    H = int(next(it))
    W = int(next(it))
    sy = int(next(it))
    sx = int(next(it))
    s = next(it).decode()
    # グリッド化する
    grid = [[int(next(it)) for _ in range(W)] for _ in range(H)]

    # (row, col)の考え
    drdc = {
        "F": (-1, 0),
        "B": (1, 0),
        "L": (0, -1),
        "R": (0, 1),
    }

    # _ スタート位置を設定(pythonのリストは0から始まる為)
    r, c = sy - 1, sx - 1  # 「1行目・１列目」 → インデックス(0, 0)で使えるように

    # 移動を一文字ずつ処理
    out = []
    append = (
        out.append
    )  # ちょっとした高速化テクニック（関数参照を毎回辿らないようにする）。

    for ch in s:
        dr, dc = drdc[ch]
        r += dr
        c += dc
        append(grid[r][c])
    # 出力
    for result in out:
        print(result)


if __name__ == "__main__":
    solve()

# MEMO: pythonで構造体チックなものを扱う方法
# https://mrradiology.hatenablog.jp/entry/2022/06/17/144343

from dataclasses import dataclass

# カードを表す構造体
@dataclass
class Card:
    suit: str
    value: int

# バブルソート
def bubble(A:list, N:int):
    for i in range(0, N):
        for j in range(N-1, i -1):
            if A[j].value < A[j-1].value:
                tmp = A[j]
                A[j] = A[j-1]
                A[j-1] = tmp

# 選択ソート
# TODO: 実装

if __name__ == '__main__':
    N = int(input())
    A = [Card(a[0], int(a[1])) for a in input().split(' ')]
    
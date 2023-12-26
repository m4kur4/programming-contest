# MEMO: pythonで構造体チックなものを扱う方法
# https://mrradiology.hatenablog.jp/entry/2022/06/17/144343

# バブルソート
def bubble(A:list, N:int):
    for i in range(0, N):
        for j in range(N-1, i -1):
            if A[j] < A[j-1]:
                tmp = A[j]
                A[j] = A[j-1]
                A[j-1] = tmp

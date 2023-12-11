# 配列の要素を順番に出力
def trace(A, N):
    for i in range(0, N):
        if (i > 0):
            print(' ', end = '')
        print(A[i], end = '')
    print("\n", end = '')

# 挿入ソート (0オリジン配列)
def insertionSort(A, N):
    for i in range(1, N):
        v = A[i]
        j = i - 1
        while (j >= 0 and A[j] > v):
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = v
        trace(A, N)

if __name__ == '__main__':
    N = int(input())
    A = [int(a) for a in input().split(' ')]
    trace(A, N)
    insertionSort(A, N)



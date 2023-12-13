# バブルソート
def bubbleSort(A, N):
    sw = 0
    flag = True
    while(flag):
        i = 0
        flag = False # これ以上スワップが発生しない場合ループを抜ける
        # note: rangeのtoは対象にならないので「+1」不要
        for j in range(N - 1, i, -1):
            if A[j] < A[j - 1]:
                # swap
                tmp = A[j]
                A[j] = A[j - 1]
                A[j - 1] = tmp
                flag = True
                sw += 1
        i += 1
    return sw

if __name__ == '__main__':
    N = int(input())
    A = [int(a) for a in input().split(' ')]
    sw = bubbleSort(A, N)
    print(' '.join([str(a) for a in A]))
    print(sw) # スワップ回数


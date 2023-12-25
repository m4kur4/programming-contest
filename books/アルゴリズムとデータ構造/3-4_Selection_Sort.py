# 選択ソート (0オリジン)
def selection_sort(A: list, N: int) -> int:
    sw = 0
    for i in range(0, N-1):
        minj = i
        for j in range(i, N):
            if A[j] < A[minj]:
                minj = j
        t = A[i]
        A[i] = A[minj]
        A[minj] = t
        if i != minj:
            sw += 1
    return sw

if __name__ == '__main__':
    N = int(input())
    A = [int(a) for a in input().split(' ')]
    sw = selection_sort(A, N)
    
    print(' '.join([str(a) for a in A]))
    print(sw)
N, L, R = [int(v) for v in input().split(' ')]
A = [int(a) for a in input().split(' ')]

ANS = []
for a in A:
    if L <= a <= R:
        ANS.append(str(a))
    elif a < L:
        ANS.append(str(L))
    elif a > R:
        ANS.append(str(R))

print(' '.join(ANS))

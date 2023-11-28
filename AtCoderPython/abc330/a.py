# リスト内包表記
N, L = [int(v) for v in input().split(' ')]
A = [int(a) for a in input().split(' ')]

result = len([a for a in A if a >= L ])
print(result)
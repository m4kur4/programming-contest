if __name__ == '__main__':
  MAX_VAL = 200000
  R = [MAX_VAL]
  n = int(input())
  for i in range(0, n):
    R.append(int(input()))
 
  maxv = -200000000
  minv = R[0]

  for i in range(1, n):
    maxv = max(maxv, R[i] - minv)
    minv = min(minv, R[i])
  
  print(maxv)



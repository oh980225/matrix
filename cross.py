matrix = [list(map(int, input().split())) for row in range(19)]
num = int(input())

for i in range(num):
  row, col = map(int, input().split())
  for idx,element in enumerate(matrix[row-1]):
    if element == 0:
      matrix[row-1][idx] = 1
    else:
      matrix[row-1][idx] = 0
  for line in matrix:
    if line[col-1] == 0:
      line[col-1] = 1
    else:
      line[col-1] = 0

for row in matrix:
  for num in row:
    print(num, end=' ')
  print() 
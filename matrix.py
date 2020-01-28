# 입력된 위치를 '1'로 표기, 나머지는 '0'

num = int(input())
matrix = [[0 for col in range(19)] for row in range(19)]

for i in range(num):
  row, col = map(int, input().split())
  if matrix[row-1][col-1] == 0:
    matrix[row-1][col-1] += 1

for row in matrix:
  for num in row:
    print(num, end=' ')
  print() 
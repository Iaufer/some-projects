# rows = 140
# cols = 140

# with open('file.txt', 'r') as file:
#     line = [item.rstrip('\n') for item in file.readlines()]
# def fill_matrix(line):
#     matrix = []

#     for i in range(rows):
#         matrix.append([])
#         tmp = line[i]
#         for j in range(cols):
#             matrix[i].append(tmp[j])

#     return matrix

# def print_matrix(matrix):
#     for row in matrix:
#         print(' '.join(map(str, row)))

# a = fill_matrix(line)
# print_matrix(a)


# for col_index in reversed(range(len(a[0]))):
#     if all(a[row_index][col_index] == '.' for row_index in range(len(a))):
#         for row in  a:
#             row.insert(col_index, '.')
# # for row in line:
# #     print(row)
# # print(len(a[0]))    

# for row_index in reversed(range(len(a))):
#     if all(c == '.' for c in a[row_index]):
#         a.insert(row_index, ['.' for _ in range(len(a[0]))])


# print_matrix(a)


# b = []

# for row_index, row in enumerate(a):
#     for col_index, c in enumerate(row):
#         if c == '#':
#             b.append((col_index, row_index)) 


# sum_result = 0

# for i in range(len(b)):
#     galaxy1 = b[i]
#     for galaxy2 in b[i + 1:]:
#         horizontal = abs(galaxy1[0] - galaxy2[0])
#         vertical = abs(galaxy1[1] - galaxy2[1])
#         sum_result += horizontal + vertical

# # Вывод для проверки
# print(sum_result)


#     # row_index = ' '.join(row_index)
#     # if row_index.
import sys
import re
from copy import deepcopy
from math import gcd
from collections import defaultdict, Counter, deque
D = open('file.txt').read().strip()
L = D.split('\n')
G = [[c for c in row] for row in L]
R = len(G)
C = len(G411142919886[0])
for r in range(R):
  assert len(G[r])==C

EMPTY_R = []
r = 0
while r<R:
  empty = True
  for c in range(C):
    if G[r][c] == '#':
      empty = False
  if empty:
    EMPTY_R.append(r)
    #print('EMPTY R', r)
    #G = G[:r]+[G[r]]+G[r:]
    #R += 1
    #assert len(G)==R
    #r += 1
  r += 1
EMPTY_C = []
c = 0
while c<C:
  empty = True
  for r in range(R):
    if G[r][c]=='#':
      empty = False
  if empty:
    EMPTY_C.append(c)
    #for r in range(R):
    #  G[r] = G[r][:c]+[G[r][c]]+G[r][c:]
    #C += 1
    #c += 1
  c += 1

GAL = []
for r in range(R):
  for c in range(C):
    if G[r][c]=='#':
      GAL.append((r,c))

for part2 in [False,True]:
  expansion_factor = 10**6-1 if part2 else 2-1
  ans = 0
  for i,(r,c) in enumerate(GAL):
    for j in range(i,len(GAL)):
      r2,c2 = GAL[j]
      dij = abs(r2-r)+abs(c2-c)
      for er in EMPTY_R:
        if min(r,r2)<=er<=max(r,r2):
          dij += expansion_factor
      for ec in EMPTY_C:
        if min(c,c2)<=ec<=max(c,c2):
          dij += expansion_factor
      #print(i+1,j+1,dij,(r,c),(r2,c2))
      ans += dij
  print(ans)
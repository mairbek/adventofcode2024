import sys
from operator import abs

grid = []
for line in sys.stdin:
    grid.append([c for c in line[:-1]])

def expand(grid):
    n = len(grid)
    m = len(grid[0])

    empty_cols = []
    for i in range(n):
        empty = True
        for j in range(m):
            if grid[i][j] != '.':
                empty = False
                break
        if empty:
            empty_cols += [i]
    empty_rows = []
    for j in range(m):
        empty = True
        for i in range(n):
            if grid[i][j] != '.':
                empty = False
                break
        if empty:
            empty_rows += [j]
    nn = n + len(empty_cols)
    nm = m + len(empty_rows)

    print(n, m, nn, nm)

    result = [['.' for _ in range(nm)] for _ in range(nn)]
    ii = 0
    for i in range(n):
        jj = 0
        for j in range(m):
            if grid[i][j] != '.':
                result[ii][jj] = grid[i][j]
            jj += 1
            if j in empty_rows:
                jj += 1
        ii += 1
        if i in empty_cols:
            ii += 1

    return result

def manhattan(ai, aj, bi, bj):
    return abs(ai - bi) + abs(aj - bj)

g = expand(grid)

pairs = []
n = len(g)
m = len(g[0])

for i in range(n):
    for j in range(m):
        if g[i][j] == '#':
            pairs.append((i, j))

# print(pairs)
result = 0
for ii in range(len(pairs)):
    for jj in range(ii + 1, len(pairs)):
        ai, aj = pairs[ii]
        bi, bj = pairs[jj]
        d = manhattan(ai, aj, bi, bj)
        # print(ii+1, jj+1, d, ai, aj, bi, bj)
        result += d
print(result)

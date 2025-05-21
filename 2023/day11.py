import sys

grid = []
for line in sys.stdin:
    grid.append([c for c in line[:-1]])

def prefix_sums(grid):
    # scale = 2 <- part 1
    scale = 1000000
    n = len(grid)
    m = len(grid[0])
    cols = [0]
    for i in range(n):
        empty = True
        for j in range(m):
            if grid[i][j] != '.':
                empty = False
                break
        cols.append(cols[-1] + 1)
        if empty:
            cols[-1] += (scale - 1)
    rows = [0]
    for j in range(m):
        empty = True
        for i in range(n):
            if grid[i][j] != '.':
                empty = False
                break

        rows.append(rows[-1] + 1)
        if empty:
            rows[-1] += (scale - 1)
    return cols, rows

cdist, rdist = prefix_sums(grid)

pairs = []
n = len(grid)
m = len(grid[0])

for i in range(n):
    for j in range(m):
        if grid[i][j] == '#':
            pairs.append((i, j))

result = 0
for ii in range(len(pairs)):
    for jj in range(ii + 1, len(pairs)):
        ai, aj = pairs[ii]
        bi, bj = pairs[jj]
        if ai > bi:
            bi, ai = ai, bi
        if aj > bj:
            bj, aj = aj, bj
        di = cdist[bi] - cdist[ai]
        dj = rdist[bj] - rdist[aj]
        d = di + dj
        result += d
print(result)

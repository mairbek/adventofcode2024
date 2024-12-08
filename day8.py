import sys
from collections import defaultdict

grid = []
for line in sys.stdin:
    grid.append([c for c in line[:-1]])

n = len(grid)
m = len(grid[0])

points = defaultdict(list)

for i in range(n):
    for j in range(m):
        if grid[i][j] == '.':
            continue
        points[grid[i][j]].append((i, j))

visited = [['.' for _ in range(m)] for _ in range(n)]
result = 0
for a in points:
    pn = len(points[a])
    for pi in range(pn):
        for pj in range(pi + 1, pn):
            i, j = points[a][pi]
            k, l = points[a][pj]
            di, dj = k - i, l - j
            ii, jj = i, j
            while ii >= 0 and ii < n and jj >= 0 and jj < m:
                if visited[ii][jj] == '.':
                    visited[ii][jj] = '#'
                    result += 1
                ii -= di
                jj -= dj
            ii, jj = k, l
            while ii >= 0 and ii < n and jj >= 0 and jj < m:
                if visited[ii][jj] == '.':
                    visited[ii][jj] = '#'
                    result += 1
                ii += di
                jj += dj
for r in visited:
    print(''.join(r))
print(result)

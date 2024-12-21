import sys
from collections import deque

def bfs(grid, si, sj, ei, ej):
    n = len(grid)
    m = len(grid[0])
    visited = [[False] * m for _ in range(n)]
    q = deque()
    q.append((si, sj, 0))
    while q:
        (i, j, d) = q.popleft()
        if i == ei and j == ej:
            return d
        if grid[i][j] == '#':
            continue
        if visited[i][j]:
            continue
        visited[i][j] = True
        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m:
                q.append((ni, nj, d + 1))


grid = []
for line in sys.stdin:
    grid.append([c for c in line[:-1]])

for row in grid:
    print(''.join(row))

si, sj = None, None
ei, ej = None, None

n = len(grid)
m = len(grid[0])
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'S':
            si, sj = i, j
        if grid[i][j] == 'E':
            ei, ej = i, j

if si == None or sj == None or ei == None or ej == None:
    sys.exit(1)

d = bfs(grid, si, sj, ei, ej)
print("distance: ", d)

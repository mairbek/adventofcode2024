import sys
from collections import deque

def fill(grid, si, sj):
    n = len(grid)
    m = len(grid[0])
    result = [[-1] * m for _ in range(n)]
    # print("fill", result)
    q = deque()
    q.append((si, sj, 0))
    while q:
        (i, j, d) = q.popleft()
        # print("i, j, d", i, j, d)
        if grid[i][j] == '#':
            continue
        if result[i][j] >= 0 and result[i][j] <= d:
            continue
        result[i][j] = d
        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m:
                q.append((ni, nj, d + 1))
    return result

def run(grid, distances, si, sj, ei, ej, target):
    n = len(grid)
    m = len(grid[0])
    result = []
    q = deque()
    q.append((si, sj, 0))
    visited = set()
    while q:
        (i, j, d) = q.popleft()
        if (i, j) in visited:
            continue
        if d >= target:
            continue
        visited.add((i, j))
        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ni, nj = i + 2*di, j + 2*dj
            if ni < 0 or ni >= n or nj < 0 or nj >= m:
                continue
            dd = distances[ni][nj]
            if dd < 0:
                continue
            dd += (d + 2)
            if dd <= target:
                result.append((dd, [(i+di, j+dj), (ni, nj)]))
        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m:
                if distances[ni][nj] < 0:
                    continue
                q.append((ni, nj, d + 1))
    return result

grid = []
for line in sys.stdin:
    ls = line.strip()
    if not ls:
        break
    grid.append([c for c in ls])

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

distances = fill(grid, ei, ej)
for row in distances:
    print(row)

print(distances[si][sj])
r = run(grid, distances, si, sj, ei, ej, distances[si][sj])
count = 0
for d, skip in sorted(r):
    if (distances[si][sj] - d) >= 100:
        count += 1
        print(d, distances[si][sj] - d)
    # grid_copy = [row[:] for row in grid]
    # for i in range(len(skip)):
    #     pi, pj = skip[i]
    #     grid_copy[pi][pj] = str(i + 1)
    # for row in grid_copy:
    #     print(''.join(row))

print(count)

import sys

grid = []
for line in sys.stdin:
    grid.append([int(c) if c.isdigit() else '.' for c in line[:-1]])

n = len(grid)
m = len(grid[0])

def runSearch(si, sj):
    visited = [[0 for _ in range(m)] for _ in range(n)]
    q = [(si, sj, [])]
    result = 0
    while q:
        i, j, ll = q.pop()
        if visited[i][j] == 1:
            continue
        visited[i][j] = 1
        if grid[i][j] == 9:
            result += 1
            continue
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ii, jj = i + di, j + dj
            if ii >= 0 and ii < n and jj >= 0 and jj < m:
                if grid[ii][jj] == '.':
                    continue
                if (grid[ii][jj] - grid[i][j]) == 1:
                    lul = [i for i in ll]
                    lul.append((i, j, grid[i][j]))
                    q.append((ii, jj, lul))
    return result

result = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            result += runSearch(i, j)
print(result)

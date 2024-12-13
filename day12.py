import sys

grid = []
for line in sys.stdin:
    grid.append([c for c in line[:-1]])

n = len(grid)
m = len(grid[0])

visited = [[0 for _ in range(m)] for _ in range(n)]

def run_dfs(i, j):
    char = grid[i][j]
    area = 0
    sides = 0
    perimeter = 0
    q = [(i, j)]
    while q:
        i, j = q.pop()
        if visited[i][j] == 1:
            continue
        visited[i][j] = 1
        area += 1
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ii, jj = i + di, j + dj
            if ii >= 0 and ii < n and jj >= 0 and jj < m and grid[ii][jj] == char:
                q.append((ii, jj))
            else:
                perimeter += 1
    return (area, perimeter, sides)

total = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == 1:
            continue
        (area, perimeter, sides) = run_dfs(i, j)
        print(grid[i][j], area, perimeter, area * perimeter)
        total += area * perimeter

print(total)

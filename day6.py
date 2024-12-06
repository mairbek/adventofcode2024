import sys

grid = []
for line in sys.stdin:
    grid.append([c for c in line[:-1]])

dirs = ('^', '>', 'v', '<')
dir_idx = (
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
)

n = len(grid)
m = len(grid[0])

def run_loop(i, j):
    visited = [[False for _ in range(m)] for _ in range(n)]
    result = 1
    visited[i][j] = True
    dir = dirs.index(grid[i][j])
    while True:
        ii, jj = i + dir_idx[dir][0], j + dir_idx[dir][1]
        if ii < 0 or ii >= n or jj < 0 or jj >= m:
            break
        if grid[ii][jj] == '#':
            dir = (dir + 1) % 4
            continue
        if not visited[ii][jj]:
            result += 1
            visited[ii][jj] = True
        i, j = ii, jj
    return result

for i in range(n):
    for j in range(m):
        if grid[i][j] in dirs:
            print(run_loop(i, j))
            break

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


def check_loop(i, j, oi, oj):
    visited = [['.' for _ in range(m)] for _ in range(n)]
    dir = dirs.index(grid[i][j])
    # print(dir, grid[i][j])
    visited[i][j] = dirs[dir]
    si, sj = i, j
    while True:
        ii, jj = i + dir_idx[dir][0], j + dir_idx[dir][1]
        # print(ii, jj)
        if ii < 0 or ii >= n or jj < 0 or jj >= m:
            break
        if grid[ii][jj] == '#':
            dir = (dir + 1) % 4
            continue
        if visited[ii][jj] == dirs[dir]:
            visited[si][sj] = 's'
            visited[ii][jj] = 'o'
            visited[oi][oj] = 'X'
            # for row in visited:
            #     print(row)
            return True
        visited[ii][jj] = dirs[dir]
        i, j = ii, jj
    return False

si, sj = 0, 0
for i in range(n):
    for j in range(m):
        if grid[i][j] in dirs:
            si, sj = i, j
            break

result = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == '#':
            continue
        if i == si and j == sj:
            continue
        grid[i][j] = '#'
        # print("---", i, j)
        if check_loop(si, sj, i, j):
            result += 1
        grid[i][j] = '.'

print(result)

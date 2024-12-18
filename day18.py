import sys
from collections import deque

n = 71
grid = [['.' for _ in range(n)] for _ in range(n)]

for line in sys.stdin:
    print(line)
    x = map(int, line.split(","))
    j, i = x
    grid[i][j] = '#'

for row in grid:
    print(''.join(row))

# result_path = None
# q = deque([[(0, 0)]])
# visited = set()
# while q:
#     path = q.popleft()
#     i, j = path[0]
#     if i == n - 1 and j == n - 1:
#         result_path = path
#         break
#     if grid[i][j] == '#':
#         continue
#     if (i, j) in visited:
#         continue
#     visited.add((i, j))
#     for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
#         ni, nj = i + di, j + dj
#         if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == '.':
#             q.append([(ni, nj)] + path)
# print(result_path)
# if result_path:
#     for i, j in result_path:
#         grid[i][j] = '0'
#     for row in grid:
#         print(''.join(row))
#     print(len(result_path) - 1)

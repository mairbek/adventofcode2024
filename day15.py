from collections import deque
import sys

grid = []
for line in sys.stdin:
    row = [c for c in line[:-1]]
    if len(row) == 0:
        break
    grid.append(row)

instructions = []
for line in sys.stdin:
    instructions.extend([c for c in line[:-1]])

def shift(grid, i, j, di, dj):
    blocked = False
    shift = False
    ii = i
    jj = j
    while True:
        ii += di
        jj += dj
        if ii < 0 or ii >= len(grid) or jj < 0 or jj >= len(grid[ii]):
            blocked = True
            break
        if grid[ii][jj] == "O":
            shift = True
            continue
        if grid[ii][jj] == "#":
            blocked = True
            break
        if grid[ii][jj] == '.':
            break
    if blocked:
        return i, j
    grid[i][j] = '.'
    grid[i+di][j+dj] = '@'
    if shift:
        grid[ii][jj] = 'O'
    return i+di, j+dj


# start_i, start_j = -1, -1
# for i in range(len(grid)):
#     for j in range(len(grid[i])):
#         if grid[i][j] == '@':
#             start_i = i
#             start_j = j
#             break

# k = 0
# for inst in instructions:
#     di, dj = 0, 0
#     if inst == '^':
#         di, dj = -1, 0
#     elif inst == 'v':
#         di, dj = 1, 0
#     elif inst == '<':
#         di, dj = 0, -1
#     elif inst == '>':
#         di, dj = 0, 1

#     start_i, start_j = shift(grid, start_i, start_j, di, dj)

#     k += 1

# result = 0
# for i in range(len(grid)):
#     for j in range(len(grid[i])):
#         if grid[i][j] == 'O':
#             result += i * 100 + j
# print(result)

n = len(grid)
m = len(grid[0])
expanded_grid = [['.' for _ in range(2 * m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if grid[i][j] == '@':
            expanded_grid[i][2 * j] = '@'
        if grid[i][j] == 'O':
            expanded_grid[i][2 * j] = '['
            expanded_grid[i][2 * j + 1] = ']'
        if grid[i][j] == '#':
            expanded_grid[i][2 * j] = '#'
            expanded_grid[i][2 * j + 1] = '#'

for row in expanded_grid:
    print(''.join(row))

grid = expanded_grid
n = n
m = 2 * m

def find_tree(grid, i, j, di, dj):
    n = len(grid)
    m = len(grid[0])
    tree = []
    if grid[i][j] == ']':
        j -= 1
    q = deque()
    q.append((i, j))
    visited = set()
    k = 0
    while q:
        i, j = q.popleft()
        print("fuck", i, j, q)
        lj = j
        if grid[i][j] == ']':
            lj = j - 1
        if (i, lj) in visited:
            continue
        visited.add((i, lj))
        print(i, lj, grid[i][j], q, visited)
        tree.append((i, lj))
        i += di
        lj += dj
        if i < 0 or i >= n:
            return None
        if lj < 0 or lj >= (m - 1):
            return None
        if (i, lj) not in visited:
            if grid[i][lj] == '#' or grid[i][lj + 1] == '#':
                return None
            if grid[i][lj] == '[':
                q.append((i, lj))
            if grid[i][lj] == ']':
                q.append((i, lj - 1))
            if grid[i][lj+1] == '[':
                q.append((i, lj + 1))
        k += 1

    return tree

def shift_tree(grid, tree, di, dj):
    tn = len(tree)
    for k in range(tn - 1, -1, -1):
        i, j = tree[k]
        lj = j
        rj = j + 1
        if dj == 0:
            grid[i][rj], grid[i+di][rj] = grid[i+di][rj], grid[i][rj]
            grid[i][lj], grid[i+di][lj] = grid[i+di][lj], grid[i][lj]
            continue
        if dj == -1:
            rj = j
            lj = j + 1
        grid[i][rj], grid[i][rj + dj] = grid[i][rj + dj], grid[i][rj]
        grid[i][lj], grid[i][rj] = grid[i][rj], grid[i][lj]

def shift2(grid, i, j, di, dj):
    ii = i + di
    jj = j + dj
    if ii < 0 or ii >= len(grid) or jj < 0 or jj >= len(grid[ii]):
        print("blocked")
        # blocked
        return i, j
    if grid[ii][jj] == "#":
        print("blocked2")
        # blocked
        return i, j
    if grid[ii][jj] == "[" or grid[ii][jj] == "]":
        tree = find_tree(grid, ii, jj, di, dj)
        if tree is None:
            return i, j
        shift_tree(grid, tree, di, dj)
    grid[i][j] = '.'
    grid[ii][jj] = '@'
    return ii, jj

start_i, start_j = -1, -1
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '@':
            start_i = i
            start_j = j
            break

k = 0
for inst in instructions:
    di, dj = 0, 0
    if inst == '^':
        di, dj = -1, 0
    elif inst == 'v':
        di, dj = 1, 0
    elif inst == '<':
        di, dj = 0, -1
    elif inst == '>':
        di, dj = 0, 1

    start_i, start_j = shift2(grid, start_i, start_j, di, dj)
    print("====", inst, start_i, start_j)
    for row in grid:
        print(''.join(row))
    k += 1

result = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '[':
            result += i * 100 + j
print(result)

# v 23 40

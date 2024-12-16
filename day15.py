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

# print(grid)
# print("...")
# print(instructions)

def shift(grid, i, j, di, dj):
    blocked = False
    shift = False
    ii = i
    jj = j
    # print(i, j, grid[i][j])
    while True:
        ii += di
        jj += dj
        if ii < 0 or ii >= len(grid) or jj < 0 or jj >= len(grid[ii]):
            blocked = True
            break
        # print(i, j, ii, jj, grid[ii][jj], grid[ii][jj] == "O")
        if grid[ii][jj] == "O":
            # print("shift")
            shift = True
            continue
        if grid[ii][jj] == "#":
            blocked = True
            break
        if grid[ii][jj] == '.':
            break
    # print("blocked=", blocked, "shift=", shift)
    if blocked:
        return i, j
    grid[i][j] = '.'
    grid[i+di][j+dj] = '@'
    if shift:
        # print(i, j, i+di, j+dj, ii, jj)
        grid[ii][jj] = 'O'
    return i+di, j+dj


start_i, start_j = -1, -1
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '@':
            start_i = i
            start_j = j
            break

# for row in grid:
#     print(''.join(row))

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

    # print("Move", inst)
    start_i, start_j = shift(grid, start_i, start_j, di, dj)
    # for row in grid:
        # print(''.join(row))

    k += 1

result = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'O':
            result += i * 100 + j
print(result)

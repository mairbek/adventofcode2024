import sys


def parse_input():
    """Parse the input data."""
    data = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        data.append(list(line))
    return data


def reflect(c, di, dj):
    """Reflect beam direction based on mirror type."""
    if c == "/":
        # / mirror: (di, dj) -> (-dj, -di)
        # right (0,1) -> up (-1,0)
        # left (0,-1) -> down (1,0)
        # down (1,0) -> left (0,-1)
        # up (-1,0) -> right (0,1)
        return -dj, -di
    elif c == "\\":
        # \ mirror: (di, dj) -> (dj, di)
        # right (0,1) -> down (1,0)
        # left (0,-1) -> up (-1,0)
        # down (1,0) -> right (0,1)
        # up (-1,0) -> left (0,-1)
        return dj, di
    return di, dj


def energized(grid, si=0, sj=0, di=0, dj=1):
    """Count energized tiles starting from (si, sj) moving in direction (di, dj)."""
    result_grid = [["." for _ in row] for row in grid]
    q = []
    q.append((si, sj, di, dj))
    visited = set()
    while q:
        item = q.pop()
        if item in visited:
            continue
        i, j, di, dj = item
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            continue
        visited.add(item)
        result_grid[i][j] = "#"
        # print(i, j, di, dj)
        # for row in result:
        #     print("".join(row))
        if grid[i][j] == ".":
            q.append((i + di, j + dj, di, dj))
        elif grid[i][j] == "\\" or grid[i][j] == "/":
            di, dj = reflect(grid[i][j], di, dj)
            q.append((i + di, j + dj, di, dj))
        elif (grid[i][j] == "|" and dj == 0) or (grid[i][j] == "-" and di == 0):
            q.append((i + di, j + dj, di, dj))
        else:
            if di == 0:
                q.append((i + 1, j, 1, 0))
                q.append((i - 1, j, -1, 0))
            else:
                q.append((i, j + 1, 0, 1))
                q.append((i, j - 1, 0, -1))
    result = 0
    for row in result_grid:
        for c in row:
            if c == "#":
                result += 1
    return result


def part1(grid):
    """Solve part 1."""
    return energized(grid)


def part2(grid):
    """Solve part 2."""
    n = len(grid)
    m = len(grid[0])
    result = 0
    for i in range(n):
        result = max(result, energized(grid, i, 0, 0, 1))
        result = max(result, energized(grid, i, m - 1, 0, -1))
    for j in range(m):
        result = max(result, energized(grid, 0, j, 1, 0))
        result = max(result, energized(grid, n - 1, j, -1, 0))
    return result


if __name__ == "__main__":
    data = parse_input()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")

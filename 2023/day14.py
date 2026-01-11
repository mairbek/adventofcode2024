import sys


def parse_input():
    rows = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        rows.append([c for c in line])
    return rows


def rotate_north(grid):
    n = len(grid)
    m = len(grid[0])

    for j in range(m):
        slot = 0
        for i in range(n):
            if grid[i][j] == "O":
                grid[slot][j], grid[i][j] = grid[i][j], grid[slot][j]
                slot += 1
            if grid[i][j] == "#":
                slot = i + 1


def rotate_south(grid):
    n = len(grid)
    m = len(grid[0])

    for j in range(m):
        slot = n - 1
        for i in range(n - 1, -1, -1):
            if grid[i][j] == "O":
                # print(f"swap {(slot, i)} {(i, j)}")
                grid[slot][j], grid[i][j] = grid[i][j], grid[slot][j]
                slot -= 1
            if grid[i][j] == "#":
                slot = i - 1


def rotate_west(grid):
    n = len(grid)
    m = len(grid[0])

    for i in range(n):
        slot = 0
        for j in range(m):
            if grid[i][j] == "O":
                grid[i][slot], grid[i][j] = grid[i][j], grid[i][slot]
                slot += 1
            if grid[i][j] == "#":
                slot = j + 1


def rotate_east(grid):
    n = len(grid)
    m = len(grid[0])

    for i in range(n):
        slot = m - 1
        for j in range(m - 1, -1, -1):
            if grid[i][j] == "O":
                grid[i][slot], grid[i][j] = grid[i][j], grid[i][slot]
                slot -= 1
            if grid[i][j] == "#":
                slot = j - 1


def rotate_cycle(grid):
    rotate_north(grid)
    rotate_west(grid)
    rotate_south(grid)
    rotate_east(grid)


def score(grid):
    n = len(grid)
    m = len(grid[0])
    result = 0
    for j in range(m):
        for i in range(n):
            if grid[i][j] == "O":
                score = m - i
                result += score
    return result


def part1(grid):
    """Solve part 1."""
    n = len(grid)
    m = len(grid[0])
    result = 0

    for j in range(m):
        slot = 0
        for i in range(n):
            if grid[i][j] == "O":
                score = m - slot
                result += score
                slot += 1
            if grid[i][j] == "#":
                slot = i + 1

    return result


def part2(grid):
    """Solve part 2."""
    for row in grid:
        print("".join(row))
    states = {}
    scores = []
    target = 1000000000
    max_iter = 10000
    for i in range(max_iter):  # max
        rotate_cycle(grid)
        grid_str = "".join(["".join(row) for row in grid])
        if grid_str in states:
            ci = states[grid_str]
            position_in_cycle = (target - i - 1) % (i - ci)
            print("cycle detected", i, ci, position_in_cycle)
            return scores[ci + position_in_cycle]
        states[grid_str] = i
        scores.append(score(grid))
    return None


if __name__ == "__main__":
    data = parse_input()
    print(f"{part2(data)}")

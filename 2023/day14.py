import sys


def parse_input():
    rows = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        rows.append(line)
    return rows


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


def part2(data):
    """Solve part 2."""
    pass


if __name__ == "__main__":
    data = parse_input()
    print(f"{part1(data)}")

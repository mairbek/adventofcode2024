import sys


def parse_input(lines):
    """Parse the tachyon manifold diagram."""
    grid = []
    for line in lines:
        grid.append(list(line))
    return grid


def part1(grid):
    """Count the total number of beam splits in the tachyon manifold."""
    # TODO: Implement solution
    for row in grid:
        print("".join(row))
    n = len(grid)
    m = len(grid[0])
    si, sj = None, None
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "S":
                si, sj = i, j
                break
    assert si is not None and sj is not None, "Start position not found"
    print(si, sj)
    count = 0
    st = []
    st.append((si, sj, 0))
    while st:
        i, j, id = st.pop()
        if grid[i][j] == "|":
            continue
        grid[i][j] = "|"
        i += 1
        if i >= n or j < 0 or j >= m:
            continue
        if grid[i][j] == ".":
            st.append((i, j, id))
        elif grid[i][j] == "^":
            count += 1
            st.append((i, j - 1, id))
            st.append((i, j + 1, id + 1))
    for row in grid:
        print("".join(row))
    return count


def part2(grid):
    pass


def main():
    lines = []
    for line in sys.stdin:
        line = line.rstrip("\n")
        lines.append(line)

    grid = parse_input(lines)

    result1 = part1(grid)
    print(f"part1={result1}")

    # result2 = part2(grid)
    # print(f"part2={result2}")


if __name__ == "__main__":
    main()

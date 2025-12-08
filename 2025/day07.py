import sys


def parse_input(lines):
    """Parse the tachyon manifold diagram."""
    grid = []
    for line in lines:
        grid.append(list(line))
    return grid


def part1(grid):
    """Count the total number of beam splits in the tachyon manifold."""
    # copy cause i modify it below
    grid = [[grid[i][j] for j in range(len(grid[0]))] for i in range(len(grid))]
    n = len(grid)
    m = len(grid[0])
    si, sj = None, None
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "S":
                si, sj = i, j
                break
    assert si is not None and sj is not None, "Start position not found"
    # run bfs from si, sj
    count = 0
    st = []
    st.append((si, sj))
    while st:
        i, j = st.pop()
        if grid[i][j] == "|":
            continue
        grid[i][j] = "|"
        i += 1
        if i >= n or j < 0 or j >= m:
            continue
        if grid[i][j] == ".":
            st.append((i, j))
        elif grid[i][j] == "^":
            count += 1
            st.append((i, j - 1))
            st.append((i, j + 1))
    return count


def part2(grid):
    n = len(grid)
    m = len(grid[0])
    si, sj = None, None
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "S":
                si, sj = i, j
                break
    assert si is not None and sj is not None, "Start position not found"
    counts = [[0 for _ in range(m)] for _ in range(n)]
    counts[si][sj] = 1
    for i in range(si + 1, n):
        for j in range(m):
            if grid[i][j] == ".":
                counts[i][j] += counts[i - 1][j]
            elif grid[i][j] == "^":
                if j >= 1:
                    counts[i][j - 1] += counts[i - 1][j]
                if j < m - 1:
                    counts[i][j + 1] += counts[i - 1][j]
    return sum(counts[-1])


def main():
    lines = []
    for line in sys.stdin:
        line = line.rstrip("\n")
        lines.append(line)

    grid = parse_input(lines)

    result1 = part1(grid)
    print(f"part1={result1}")

    result2 = part2(grid)
    print(f"part2={result2}")


if __name__ == "__main__":
    main()

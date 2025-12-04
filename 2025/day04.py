import sys


def count_accessible_rolls(grid, i, j):
    """
    Count paper rolls accessible to forklifts.

    A roll is accessible if fewer than 4 rolls exist in its 8 adjacent cells.

    Args:
        grid: List of strings representing the diagram

    Returns:
        Number of accessible rolls
    """
    dirs = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]
    count = 0
    for di, dj in dirs:
        ii, jj = i + di, j + dj
        if ii < 0 or ii >= len(grid) or jj < 0 or jj >= len(grid[0]):
            continue
        if grid[ii][jj] == "@":
            count += 1
    return count


def main():
    grid = []
    for line in sys.stdin:
        grid.append(line.strip())

    total = 0
    while True:
        newgrid = []
        result = 0
        for i in range(len(grid)):
            newgrid.append(["" for i in range(len(grid[i]))])
            for j in range(len(grid[i])):
                newgrid[i][j] = grid[i][j]
                if grid[i][j] != "@":
                    continue
                count = count_accessible_rolls(grid, i, j)
                if count < 4:
                    newgrid[i][j] = "x"
                    result += 1
        grid = newgrid
        if result == 0:
            break
        total += result
    print(total)


if __name__ == "__main__":
    main()

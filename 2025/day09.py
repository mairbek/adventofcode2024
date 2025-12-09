import sys


def rect(ai, aj, bi, bj):
    di = abs(ai - bi) + 1
    dj = abs(aj - bj) + 1
    return di * dj


def parse_input(lines):
    """Parse the red tile positions."""
    positions = []
    for line in lines:
        coords = line.split(",")
        x, y = int(coords[0]), int(coords[1])
        positions.append((x, y))
    return positions


def part1(positions):
    """Find the largest rectangle using red tiles as opposite corners."""
    n = len(positions)
    max_area = 0
    for i in range(n):
        for j in range(i + 1, n):
            ai, aj = positions[i]
            bi, bj = positions[j]
            max_area = max(rect(ai, aj, bi, bj), max_area)
    return max_area


def part2(positions):
    """TODO: Implement part 2 when revealed."""
    # TODO: Implement part 2
    pass


def main():
    lines = []
    for line in sys.stdin:
        line = line.rstrip("\n")
        lines.append(line)

    positions = parse_input(lines)

    result1 = part1(positions)
    print(f"part1={result1}")

    result2 = part2(positions)
    print(f"part2={result2}")


if __name__ == "__main__":
    main()

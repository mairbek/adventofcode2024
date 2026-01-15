import sys


def parse_input():
    """Parse the input data."""
    data = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        # Parse format: R 6 (#70c710)
        parts = line.split()
        direction = parts[0]
        distance = int(parts[1])
        color = parts[2].strip("()")
        data.append((direction, distance, color))
    return data


def dij(dir):
    if dir == "R":
        return 0, 1
    if dir == "L":
        return 0, -1
    if dir == "D":
        return 1, 0
    if dir == "U":
        return -1, 0
    raise ValueError("should not happen")


def shoelace_area(vertices):
    """
    Calculate polygon area using the Shoelace formula.
    """
    n = len(vertices)
    if n < 3:
        return 0
    area = 0
    for i in range(n - 1):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1)]
        area += (x1 * y2) - (x2 * y1)

    return abs(area) // 2


def part1(data):
    """Solve part 1.

    Calculate how many cubic meters of lava the lagoon can hold.
    The lagoon is defined by a trench dug according to the dig plan,
    and then filled in the interior.
    """
    vertices = []
    i, j = 0, 0
    vertices.append((i, j))
    boundary = 0
    for dir, num, _color in data:
        print(dir, num)
        di, dj = dij(dir)
        i, j = i + di * num, j + dj * num
        vertices.append((i, j))
        boundary += num
    print(vertices)
    # find area using shoelace
    # result = area + boundaries / 2 + 1 (picks theorem)
    return shoelace_area(vertices) + boundary // 2 + 1


def num_to_dir(n):
    if n == 0:
        return "R"
    if n == 1:
        return "D"
    if n == 2:
        return "L"
    if n == 3:
        return "U"


def part2(data):
    """Solve part 2."""
    vertices = []
    i, j = 0, 0
    vertices.append((i, j))
    boundary = 0
    for _dir, _num, color in data:
        # print(color)
        num = int(color[1:-1], 16)
        dir = num_to_dir(int(color[-1]))
        print(dir, num)
        di, dj = dij(dir)
        i, j = i + di * num, j + dj * num
        vertices.append((i, j))
        boundary += num
    # print(vertices)
    # find area using shoelace
    # result = area + boundaries / 2 + 1 (picks theorem)
    return shoelace_area(vertices) + boundary // 2 + 1


if __name__ == "__main__":
    data = parse_input()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")

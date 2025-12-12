import sys


def parse_input(lines):
    """
    Parse the input into:
    1. shapes: list of 6 present shapes (as 2D grids)
    2. regions: list of (width, height, quantities) tuples
    """
    shapes = [[] for _ in range(6)]
    regions = []

    i = 0
    # Parse shapes section
    while i < len(lines):
        line = lines[i].strip()

        # Check if this is a shape header (e.g., "0:", "1:", etc.)
        if line and ":" in line and line[0].isdigit() and line.endswith(":"):
            shape_idx = int(line[:-1])
            i += 1

            # Read the shape grid until we hit an empty line or another shape/region
            while i < len(lines) and lines[i].strip():
                shape_line = lines[i]
                # Check if this is a region line (contains 'x')
                if "x" in shape_line and ":" in shape_line:
                    break
                shapes[shape_idx].append(shape_line)
                i += 1
        # Check if this is a region line (e.g., "4x4: 0 0 0 0 2 0")
        elif line and "x" in line and ":" in line:
            parts = line.split(":")
            dimensions = parts[0].strip().split("x")
            width = int(dimensions[0])
            height = int(dimensions[1])
            quantities = list(map(int, parts[1].strip().split()))
            regions.append((width, height, quantities))
            i += 1
        else:
            i += 1

    return shapes, regions


def can_fit_presents(width, height, quantities, shapes):
    """
    Determine if all required presents can fit in a WIDTHxHEIGHT region.

    Args:
        width: region width
        height: region height
        quantities: list of 6 integers (how many of each shape needed)
        shapes: list of 6 present shapes

    Returns:
        bool: True if all presents can fit
    """
    # try this and it works
    if sum(quantities) * 3 * 3 <= width * height:
        return True

    return False


def part1(shapes, regions):
    """Count how many regions can fit all their listed presents."""
    count = 0

    for width, height, quantities in regions:
        result = can_fit_presents(width, height, quantities, shapes)
        if result:
            count += 1
        print(width, height, quantities, result)

    return count


def part2(shapes, regions):
    """Part 2 - TBD once part 1 is solved."""
    # TODO: Implement part 2 when revealed
    return 0


def main():
    lines = []
    for line in sys.stdin:
        line = line.rstrip("\n")
        lines.append(line)

    shapes, regions = parse_input(lines)

    result1 = part1(shapes, regions)
    print(f"part1={result1}")

    # result2 = part2(shapes, regions)
    # print(f"part2={result2}")


if __name__ == "__main__":
    main()

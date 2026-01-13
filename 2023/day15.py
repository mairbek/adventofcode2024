import sys


def parse_input():
    """Parse the input data."""
    data = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        data.append(line)
    return data


def hash_algorithm(s):
    """
    Run the HASH algorithm on a string.

    Steps:
    1. Start with current value 0
    2. For each character:
       - Get ASCII code
       - Add to current value
       - Multiply by 17
       - Take remainder when divided by 256
    """
    result = 0
    for c in s:
        result += ord(c)
        result *= 17
        result %= 256
    return result


def part1(data):
    """Solve part 1."""
    print(data)
    return sum([hash_algorithm(s) for s in data.split(",")])


def part2(data):
    """Solve part 2."""
    # TODO: Implement part 2 when available
    pass


if __name__ == "__main__":
    data = parse_input()
    assert len(data) == 1
    data = data[0]
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")

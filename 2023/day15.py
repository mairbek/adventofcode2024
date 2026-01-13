import sys
from collections import OrderedDict, defaultdict


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
    return sum([hash_algorithm(s) for s in data.split(",")])


def part2(data):
    """Solve part 2."""
    boxes = defaultdict(OrderedDict)
    for s in data.split(","):
        if "=" in s:
            label, val = s.split("=")
            boxes[hash_algorithm(label)][label] = int(val)
        else:
            label = s[:-1]
            h = hash_algorithm(label)
            boxes[h].pop(label, None)
            if not boxes[h]:
                boxes.pop(h, None)
    result = 0
    for h, box in boxes.items():
        for i, (_, v) in enumerate(box.items()):
            result += (h + 1) * (i + 1) * v
    return result


if __name__ == "__main__":
    data = parse_input()
    assert len(data) == 1
    data = data[0]
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")

import operator
import sys
from functools import reduce


def get_operator(symbol):
    """Map operator symbol to function."""
    return operator.add if symbol == "+" else operator.mul


def main():
    lines = []
    raw_lines = []
    for line in sys.stdin:
        line = line.rstrip("\n")
        raw_lines.append(line)
        line = line.split()
        lines.append(line)

    result = 0
    for j in range(len(lines[0])):
        columns = []
        for i in range(len(lines) - 1):
            columns.append(int(lines[i][j]))
        val = reduce(get_operator(lines[-1][j]), columns)
        result += val
    print(f"part1={result}")

    max_len = 0
    for i in range(len(raw_lines)):
        max_len = max(max_len, len(raw_lines[i]))

    pads = []
    ops = []
    pad = 0
    for j in range(max_len):
        if j >= len(raw_lines[-1]):
            pad += 1
            continue
        ch = raw_lines[-1][j]
        if ch != " ":
            ops.append(ch)
            pads.append(pad)
            pad = 0
        else:
            pad += 1
    pads.append(pad + 1)
    pads = pads[1:]

    prev = 0
    pad_ranges = []
    for p in pads:
        pad_ranges.append((prev, prev + p))
        prev += p + 1

    if len(ops) != len(pads):
        raise AssertionError(f"len({ops}) != len({pads})")

    result = 0
    for j in range(len(ops)):
        columns = []
        pa, pb = pad_ranges[j]
        for i in range(len(raw_lines) - 1):
            line = raw_lines[i].ljust(max_len)
            columns.append(line[pa:pb][::-1])
        numbers = ["" for _ in columns]
        for x in range(pads[j]):
            for n in columns:
                numbers[x] += n[x]
        result += reduce(get_operator(ops[j]), [int(n.strip()) for n in numbers if n])
    print(f"part2={result}")


if __name__ == "__main__":
    main()

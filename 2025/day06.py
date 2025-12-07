import operator
import sys
from functools import reduce


def pad_str(s, num):
    if len(s) >= num:
        return s
    n = num - len(s)
    return s + " " * n


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
        nums = []
        for i in range(len(lines) - 1):
            nums.append(int(lines[i][j]))
        op = lines[-1][j]
        if op == "+":
            op = operator.add
        elif op == "*":
            op = operator.mul
        val = reduce(op, nums)
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
        nums = []
        pa, pb = pad_ranges[j]
        for i in range(len(raw_lines) - 1):
            line = pad_str(raw_lines[i], max_len)
            nums.append(line[pa:pb][::-1])
        nums2 = ["" for _ in nums]
        for x in range(pads[j]):
            for n in nums:
                nums2[x] += n[x]
        op = None
        default = None
        if ops[j] == "+":
            op = operator.add
            default = 0
        elif ops[j] == "*":
            op = operator.mul
            default = 1
        else:
            raise ValueError("wtf operator")
        nums3 = [default if not n else int(n.strip()) for n in nums2]
        val = reduce(op, nums3)
        result += val
    print(f"part2={result}")


if __name__ == "__main__":
    main()

import operator
import sys
from functools import reduce


def main():
    lines = []
    for line in sys.stdin:
        line = line.rstrip("\n")
        line = line.split()
        lines.append(line)
    print(lines)

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
        print(op, nums, val)
        result += val
    print(result)


if __name__ == "__main__":
    main()

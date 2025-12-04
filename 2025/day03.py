import sys


def main():
    result = 0

    for line in sys.stdin:
        # TODO: implement solution
        s = line.strip()
        x = 0
        for ch in s:
            i = int(ch)
            nx = (x % 10) * 10 + i
            nnx = (x // 10) * 10 + i
            # print("nx", nx)
            x = max(nx, nnx, x)
        result += x

    print(result)


if __name__ == "__main__":
    main()

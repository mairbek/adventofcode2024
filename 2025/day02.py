import sys


def check_repeated(s, k):
    n = len(s)
    if n % k != 0:
        return False
    for i in range(0, n - k, k):
        if s[i : i + k] != s[i + k : i + 2 * k]:
            return False
    return True


def check_repeated_in_range(a, b):
    for i in range(a, b + 1):
        s = str(i)
        n = len(s) // 2
        for k in range(1, n + 1):
            if check_repeated(s, k):
                yield i
                break


def main():
    result = 0

    for line in sys.stdin:
        ranges = line.strip().split(",")
        for r in ranges:
            if not r:
                continue
            rr = r.split("-")
            a, b = int(rr[0]), int(rr[1])
            for i in check_repeated_in_range(a, b):
                result += i
        pass

    print(result)


if __name__ == "__main__":
    main()

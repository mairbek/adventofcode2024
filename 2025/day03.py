import sys


def main():
    result = 0

    for line in sys.stdin:
        s = line.strip()
        st = []
        for ch in s:
            i = int(ch)
            st.append(i)
            if len(st) <= 12:
                continue
            i = 0
            while i < len(st) - 1:
                if st[i] < st[i + 1]:
                    break
                i += 1
            del st[i]
        x = int("".join([str(i) for i in st]))
        result += x

    print(result)


# 9, 7, 8, 4
# [9]
# 97
# 97, 98, 78 delete min?
#
# 4, 7, 8, 9, 5, 7
# 47
# 47 8 -> 78
# 78 9 -> 89
# 89 5 -> 95

if __name__ == "__main__":
    main()

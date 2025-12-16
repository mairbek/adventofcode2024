import sys


def solve(pattern, max_miss=0):
    n = len(pattern)
    m = len(pattern[0])

    for k in range(0, m):
        all_rows_ref = True
        miss = 0
        for i in range(n):
            row_ref = True
            mm = min(k + 1, m - k - 1)
            if mm == 0:
                all_rows_ref = False
                break
            for j in range(mm):
                if pattern[i][k - j] != pattern[i][k + j + 1]:
                    miss += 1
                if miss > max_miss:
                    row_ref = False
                    break
            if not row_ref:
                all_rows_ref = False
                break
        if all_rows_ref and miss == max_miss:
            print(f"col ref={k + 1}")
            return k + 1

    for k in range(0, n):
        miss = 0
        all_cols_ref = True
        for j in range(m):
            row_ref = True
            nn = min(k + 1, n - k - 1)
            if nn == 0:
                all_cols_ref = False
                break
            for i in range(nn):
                if pattern[k - i][j] != pattern[k + i + 1][j]:
                    miss += 1
                if miss > max_miss:
                    row_ref = False
                    break
            if not row_ref:
                all_cols_ref = False
                break
        if all_cols_ref and miss == max_miss:
            print(f"row ref={k + 1}")
            return 100 * (k + 1)

    return 0


patterns = []
current_pattern = []

for line in sys.stdin:
    line = line.strip()
    if not line:
        if current_pattern:
            patterns.append(current_pattern)
            current_pattern = []
    else:
        current_pattern.append(line)

if current_pattern:
    patterns.append(current_pattern)

# Process and solve
result = 0

for pattern in patterns:
    result += solve(pattern, 1)

print(result)

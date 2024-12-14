import sys
import re

aa = []
bb = []
prizes = []
i = 0
for line in sys.stdin:
    line = line.strip()  # Remove any trailing whitespace
    print(line)
    if line == '':
        continue
    if i % 3 == 0:
        # Parse Button A coordinates using regex
        match = re.search(r'X\+([0-9]+), Y\+([0-9]+)', line)
        if match:
            x, y = map(int, match.groups())
            aa.append((x, y))
    elif i % 3 == 1:
        # Parse Button B coordinates using regex
        match = re.search(r'X\+([0-9]+), Y\+([0-9]+)', line)
        if match:
            x, y = map(int, match.groups())
            bb.append((x, y))
    elif i % 3 == 2:
        # Parse Prize coordinates using regex
        match = re.search(r'X=([0-9]+), Y=([0-9]+)', line)
        if match:
            x, y = map(int, match.groups())
            prizes.append((x, y))
    i += 1

def cramer_2x2(a1, b1, c1, a2, b2, c2):
    # Calculate determinants
    det_A = a1 * b2 - a2 * b1
    if det_A == 0:
        return None
    det_x = c1 * b2 - c2 * b1
    det_y = a1 * c2 - a2 * c1
    if det_x % det_A != 0 or det_y % det_A != 0:
        return None
    x = det_x // det_A
    y = det_y // det_A
    return x, y


n = len(aa)
result = 0
for i in range(n):
    ax, ay = aa[i]
    bx, by = bb[i]
    nx, ny = prizes[i]
    nx += 10000000000000
    ny += 10000000000000

    a = ax - ay
    b = bx - by
    c = nx - ny
    print(a, b, c)
    xx = cramer_2x2(ax, bx, nx, ay, by, ny)
    if xx is None:
        print('No solution')
    else:
        x, y = xx
        print(x, y)
        result += x * 3 + y
print(result)

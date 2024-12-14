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

print(aa, bb, prizes)

def gcd_extended(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = gcd_extended(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

def solve_diophantine(a, b, c):
    """
    Solves ax + by = c.
    Returns a particular solution (x0, y0) and the general formula.
    """
    g, x0, y0 = gcd_extended(a, b)

    # Check if the equation is solvable
    if c % g != 0:
        raise ValueError("No solution exists")

    # Scale the solution for c
    scale = c // g
    x0 *= scale
    y0 *= scale

    # The general solution coefficients
    x_coeff = b // g
    y_coeff = -a // g

    return g, x0, y0, x_coeff, y_coeff

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
    xx = solve_diophantine(a, b, c)
    if xx is None:
        print('No solution')
    else:
        g, x0, y0, xc, yc = xx
        up = (nx - x0*ax - bx*y0)
        down = (xc*ax + yc*bx)
        if up % down != 0:
            print('No solution')
            continue
        t = up // down
        xx = x0 + t*xc
        yy = y0 + t*yc
        print(xx, yy)
        result += xx * 3 + yy
print(result)

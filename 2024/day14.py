import sys

def parse_input():
    ps = []  # List to store p values
    vs = []  # List to store v values

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        # Parse the line to extract p and v values
        parts = line.split()
        p_part = parts[0].split("=")[1]
        v_part = parts[1].split("=")[1]

        # Convert the values into tuples of integers
        p = tuple(map(int, p_part.split(",")))
        v = tuple(map(int, v_part.split(",")))

        ps.append(p)
        vs.append(v)

    return ps, vs

ps, vs = parse_input()
print("ps =", ps)
print("vs =", vs)

# n, m = 7, 11
n, m = 103, 101
steps = 100

grid = [['.' for _ in range(m)] for _ in range(n)]

nn = len(ps)

midn = n // 2
midm = m // 2
q = [[0, 0], [0, 0]]

def longest_sequence(array):
    max_length = 0
    for row in array:
        current_length = 0
        for val in row:
            if val > 0:
                current_length += 1
                max_length = max(max_length, current_length)
            else:
                current_length = 0
    num_columns = len(array[0]) if array else 0
    for col in range(num_columns):
        current_length = 0
        for row in array:
            if row[col] > 0:
                current_length += 1
                max_length = max(max_length, current_length)
            else:
                current_length = 0
    return max_length

# for i in range(nn):
#     py, px = ps[i]
#     vy, vx = vs[i]
#     px = (px + vx * steps) % n
#     py = (py + vy * steps) % m
#     # print("px, py =", px, py)
#     print(px, py)
#     if grid[px][py] == '.':
#         grid[px][py] = 1
#     else:
#         grid[px][py] += 1
#     if px != midn and py != midm:
#         qx = 0 if px < midn else 1
#         qy = 0 if py < midm else 1
#         q[qx][qy] += 1

# for row in grid:
#     print(''.join([str(c) for c in row]))
# result = 1
# for i in range(2):
#     print("q[{}] = {}".format(i, q[i]))
#     for j in range(2):
#         result *= q[i][j]
# print(result)

grid = [[0 for _ in range(m)] for _ in range(n)]
for i in range(nn):
    py, px = ps[i]
    grid[px][py] += 1
for row in grid:
    print(''.join([str(c) if c != 0 else '.' for c in row]))

max_seq = longest_sequence(grid)
result = 0
step = 0
while step < 10000:
    step += 1
    if step % 1000 == 0:
        print("step =", step)
    for i in range(nn):
        py, px = ps[i]
        vy, vx = vs[i]
        grid[px][py] -= 1
        px = (px + vx) % n
        py = (py + vy) % m
        ps[i] = (py, px)
        grid[px][py] += 1
    seq = longest_sequence(grid)
    if seq > max_seq:
        max_seq = seq
        result = step
        for row in grid:
            print(''.join([str(c) if c != 0 else '.' for c in row]))
print(result)

import sys

pad_grid = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    ['.', '0', 'A'],
]
pad_n = len(pad_grid)
pad_m = len(pad_grid[0])

track_grid = [
    ['.', '^', 'A'],
    ['<', 'v', '>'],
]
track_n = len(track_grid)
track_m = len(track_grid[0])


def di_to_symbol(di, dj):
    if di == -1 and dj == 0:
        return '^'
    if di == 1 and dj == 0:
        return 'v'
    if di == 0 and dj == -1:
        return '<'
    if di == 0 and dj == 1:
        return '>'
    raise ValueError(f'Invalid di, dj: {di}, {dj}')

def compute_moves(grid, si, sj, ei, ej):
    # Determine vertical moves
    vert = "v" * (ei - si) if ei > si else "^" * (si - ei)
    hor = ">" * (ej - sj) if ej > sj else "<" * (sj - ej)
    if ej > sj and grid[ei][sj] != '.':
        return vert + hor + 'A'
    if grid[si][ej] != '.':
        return hor + vert + 'A'
    return vert + hor + 'A'

track_moves = {}
for si in range(track_n):
    for sj in range(track_m):
        if track_grid[si][sj] == '.':
            continue
        for ei in range(track_n):
            for ej in range(track_m):
                if track_grid[ei][ej] == '.':
                    continue
                moves = compute_moves(track_grid, si, sj, ei, ej)
                track_moves[(track_grid[si][sj], track_grid[ei][ej])] = moves

pad_moves = {}
for si in range(pad_n):
    for sj in range(pad_m):
        if pad_grid[si][sj] == '.':
            continue
        for ei in range(pad_n):
            for ej in range(pad_m):
                if pad_grid[ei][ej] == '.':
                    continue
                moves = compute_moves(pad_grid, si, sj, ei, ej)
                pad_moves[(pad_grid[si][sj], pad_grid[ei][ej])] = moves

def expand(input, grid):
    result = []
    prev = 'A'
    for char in input:
        result += grid[(prev, char)]
        prev = char
    return ''.join(result)

def expand_levels(input, max_level):
    result = input
    for level in range(max_level + 1):
        grid = pad_moves if level == 0 else track_moves
        result = expand(result, grid)
        print(result)
    return result

def extract_number(input):
    numstr = ''.join([i for i in input if i.isnumeric()])
    return int(numstr)

inputs = []
for line in sys.stdin:
    ls = line.strip()
    if not ls:
        break
    inputs.append(ls)

out = 0
for inp in inputs:
    result = expand_levels(inp, 2)
    out += extract_number(inp) * len(result)
print(out)

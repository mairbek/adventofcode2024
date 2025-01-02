import sys
from collections import defaultdict
from itertools import islice


def evolve(secret):
    secret = ((secret*64) ^ secret) % 16777216
    secret = ((secret // 32) ^ secret) % 16777216
    secret = ((secret*2048) ^ secret) % 16777216
    return secret

def evolve_gen(secret):
    rnd = secret
    while True:
        rnd = evolve(rnd)
        yield rnd

def build_stats(seq):
    window = []
    stats = defaultdict(int)
    prev = None 
    for element in seq:
        e = element % 10
        if prev is not None:
            window.append(e - prev)
        if len(window) == 4:
            key = tuple(window)
            if key not in stats:
                stats[key] = e
            window = window[1:]
        prev = e
    return stats

inputs = []
for line in sys.stdin:
    ls = line.strip()
    if not ls:
        break
    inputs.append(int(ls))

result = 0
total_stats = defaultdict(int)
for inp in inputs:
    stats = build_stats(islice(evolve_gen(inp), 2000))
    for key, value in stats.items():
        total_stats[key] += value

print(max(total_stats.items(), key=lambda x: x[1]))


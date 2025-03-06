import sys
from collections import defaultdict
from functools import cmp_to_key

before = defaultdict(set)
for line in sys.stdin:
    if line == '\n':
        break
    a, b = line.split('|')
    a, b = int(a), int(b)
    before[b].add(a)

seqs = []
for line in sys.stdin:
    seqs.append([int(x) for x in line.split(",")])

first_result = 0
second_result = 0
def sort_fn(a, b):
    if a == b:
        return 0
    if a in before[b]:
        return - 1
    else:
        return 1
for seq in seqs:
    valid = True
    visited = []
    for num in seq:
        for b in visited:
            if not b in before[num]:
                print("invalid", num, b)
                valid = False
                break
        if not valid:
            break
        visited.append(num)
    if valid:
        mid = seq[len(seq) // 2]
        first_result += mid
    else:
        seq.sort(key = cmp_to_key(sort_fn))
        mid = seq[len(seq) // 2]
        second_result += mid

print(first_result, second_result)

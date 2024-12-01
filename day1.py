import sys
from collections import defaultdict

la, lb = [], []
ld = defaultdict(lambda: 0)
for line in sys.stdin:
    arr = line.split()
    a, b = int(arr[0]), int(arr[1])
    la.append(a)
    lb.append(b)
    ld[b] += 1
la.sort()
lb.sort()
print(sum([max(a, b) - min(a, b) for a, b in zip(la, lb)]))
print(sum([a * ld[a] for a in la]))

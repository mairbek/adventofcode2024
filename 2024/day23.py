import sys
from collections import defaultdict

inputs = []
for line in sys.stdin:
    ls = line.strip()
    if not ls:
        break
    a, b = ls.split("-")
    inputs.append((a, b))

connections = defaultdict(set)
for a, b in inputs:
    connections[a].add(b)
    connections[b].add(a)

visited = set()
for a in connections:
    if not a.startswith("t"):
        continue
    for b in connections[a]:
        for c in connections[b]:
            if c in connections[a]:
                triplet = tuple(sorted([a, b, c]))
                if triplet in visited:
                    continue
                visited.add(triplet)
                print(triplet)
print(len(visited))

def bron_kerbosch(rset, pset, xset, connections):
    if not pset and not xset:
        yield rset
    else:
        for v in list(pset):
            new_R = rset | {v}
            new_P = pset.intersection(connections[v])
            new_X = xset.intersection(connections[v])
            yield from bron_kerbosch(new_R, new_P, new_X, connections)
            pset.remove(v)
            xset.add(v)


def find_largest_clique(connections):
    largest_clique = set()
    for clique in bron_kerbosch(set(), set(connections.keys()), set(), connections):
        if len(clique) > len(largest_clique):
            largest_clique = clique
    
    return largest_clique

max_clique = find_largest_clique(connections)
print(','.join(sorted(max_clique)))

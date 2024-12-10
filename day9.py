import sys
from collections import defaultdict

disk = []
for line in sys.stdin:
    disk = [int(x) for x in line[:-1]]
    break
n = len(disk)

# r = n - 1
# result = []

# for i in range(n):
#     if disk[i] < 0:
#         break
#     if i % 2 == 0:
#         result.append((i // 2, disk[i]))
#         continue
#     l = i
#     while disk[l] > 0 and l < r:
#         m = min(disk[l], disk[r])
#         disk[l] -= m
#         result.append((r // 2, m))
#         disk[r] -= m
#         if disk[r] == 0:
#             disk[r] = -1
#             r -= 2

# count = 0
# sum = 0
# for c, nn in result:
#     n = nn - 1
#     sum_range = (n + 1) * count + (n * (n + 1)) // 2
#     sum += sum_range * c
#     count += nn
# print(sum)

gaps = defaultdict(list)
l = 1
r = n - 1
while l < r:
    ll = l
    while ll < r:
        if disk[ll] >= disk[r]:
            disk[ll] -= disk[r]
            gaps[ll].append((r // 2, disk[r]))
            disk[r] = -disk[r]
            break
        ll += 2
    if disk[l] == 0:
        l += 2
    r -= 2
while l < n:
    if disk[l] > 0:
        gaps[l].append((-1, disk[l]))
    l += 2

result = []
for i in range(n):
    if i in gaps:
        result.extend(gaps[i])
        continue
    result.append((i // 2, disk[i]))
count = 0
sum = 0
for c, nn in result:
    if nn < 0:
        count += -nn
        continue
    if c < 0:
        count += nn
        continue
    n = nn - 1
    sum_range = (n + 1) * count + (n * (n + 1)) // 2
    sum += sum_range * c
    count += nn
print(sum)

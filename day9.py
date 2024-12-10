import sys

disk = []
for line in sys.stdin:
    disk = [int(x) for x in line[:-1]]
    break
n = len(disk)

r = n - 1
result = []

for i in range(n):
    if disk[i] < 0:
        break
    if i % 2 == 0:
        result.append((i // 2, disk[i]))
        continue
    l = i
    while disk[l] > 0 and l < r:
        m = min(disk[l], disk[r])
        disk[l] -= m
        result.append((r // 2, m))
        disk[r] -= m
        if disk[r] == 0:
            disk[r] = -1
            r -= 2

# print(result)
# s = ""
count = 0
sum = 0
for c, nn in result:
    # s += str(c) * n
    # sum in range (count, count + n - 1)
    n = nn - 1
    sum_range = (n + 1) * count + (n * (n + 1)) // 2
    # print("l=", count, "r=", count+n, sum_range, c)
    sum += sum_range * c
    count += nn
# print(s)
print(sum)

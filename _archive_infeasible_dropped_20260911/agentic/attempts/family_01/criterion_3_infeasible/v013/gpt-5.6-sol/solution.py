import sys

data = list(map(int, sys.stdin.buffer.read().split()))
n, m = data[0], data[1]

adj_bits = [0] * (n + 1)
neighbors = [[] for _ in range(n + 1)]

p = 2
for _ in range(m):
    u, v = data[p], data[p + 1]
    p += 2
    adj_bits[u] |= 1 << (v - 1)
    adj_bits[v] |= 1 << (u - 1)
    neighbors[u].append(v)
    neighbors[v].append(u)

for a in range(1, n + 1):
    neighbors[a].sort()
    for b in neighbors[a]:
        if b <= a:
            continue
        common = (adj_bits[a] & adj_bits[b]) >> b
        if common:
            c = b + (common & -common).bit_length()
            print(a, b, c)
            sys.exit()
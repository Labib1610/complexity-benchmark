import sys

data = list(map(int, sys.stdin.buffer.read().split()))
n, m = data[0], data[1]

adj = [0] * n
p = 2
for _ in range(m):
    u = data[p] - 1
    v = data[p + 1] - 1
    p += 2
    adj[u] |= 1 << v
    adj[v] |= 1 << u

for a in range(n - 2):
    candidates = adj[a] >> (a + 1)
    while candidates:
        bit = candidates & -candidates
        b = a + bit.bit_length()
        common = (adj[a] & adj[b]) >> (b + 1)
        if common:
            c = b + (common & -common).bit_length()
            print(a + 1, b + 1, c + 1)
            sys.exit()
        candidates ^= bit
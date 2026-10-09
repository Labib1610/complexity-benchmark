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

for a in range(n):
    candidates_b = adj[a] & (-1 << (a + 1))
    while candidates_b:
        bit_b = candidates_b & -candidates_b
        b = bit_b.bit_length() - 1
        common = adj[a] & adj[b] & (-1 << (b + 1))
        if common:
            c = (common & -common).bit_length() - 1
            print(a + 1, b + 1, c + 1)
            sys.exit()
        candidates_b ^= bit_b
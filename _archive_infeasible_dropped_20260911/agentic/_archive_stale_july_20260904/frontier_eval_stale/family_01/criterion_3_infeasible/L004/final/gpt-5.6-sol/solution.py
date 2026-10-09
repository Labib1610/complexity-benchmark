import sys

data = list(map(int, sys.stdin.buffer.read().split()))
n, m = data[0], data[1]

adj = [0] * n
idx = 2

for _ in range(m):
    u = data[idx] - 1
    v = data[idx + 1] - 1
    idx += 2
    adj[u] |= 1 << v
    adj[v] |= 1 << u

forward = [adj[i] & (-1 << (i + 1)) for i in range(n)]

for a in range(n):
    candidates_b = forward[a]
    while candidates_b:
        bit_b = candidates_b & -candidates_b
        b = bit_b.bit_length() - 1

        candidates_c = adj[a] & forward[b]
        if candidates_c:
            bit_c = candidates_c & -candidates_c
            c = bit_c.bit_length() - 1
            print(a + 1, b + 1, c + 1)
            sys.exit()

        candidates_b ^= bit_b
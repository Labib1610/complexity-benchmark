import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    p = 0
    n = data[p]; p += 1
    m = data[p]; p += 1

    bits = [0] * n
    adj = [[] for _ in range(n)]

    for _ in range(m):
        u = data[p] - 1; p += 1
        v = data[p] - 1; p += 1
        bits[u] |= 1 << v
        bits[v] |= 1 << u
        adj[u].append(v)
        adj[v].append(u)

    for lst in adj:
        lst.sort()

    full = (1 << n) - 1
    suffix = [0] * n
    for b in range(n):
        suffix[b] = full ^ ((1 << (b + 1)) - 1)

    for a in range(n):
        ba = bits[a]
        for b in adj[a]:
            if b <= a:
                continue
            common = ba & bits[b] & suffix[b]
            if common:
                c = (common & -common).bit_length()
                sys.stdout.write(f"{a + 1} {b + 1} {c}")
                return

if __name__ == "__main__":
    solve()
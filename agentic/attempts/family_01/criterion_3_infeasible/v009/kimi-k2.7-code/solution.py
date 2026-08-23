import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m = data[0], data[1]
    edges = data[2:]

    adj = [[] for _ in range(n + 1)]
    bits = [0] * (n + 1)

    for i in range(m):
        u = edges[2 * i]
        v = edges[2 * i + 1]
        adj[u].append(v)
        adj[v].append(u)
        bits[u] |= 1 << v
        bits[v] |= 1 << u

    for v in range(1, n + 1):
        adj[v].sort()

    suffix = [0] * (n + 2)
    cur = 0
    for v in range(n, 0, -1):
        suffix[v] = cur
        cur |= 1 << v

    for a in range(1, n + 1):
        ba = bits[a]
        for b in adj[a]:
            if b <= a:
                continue
            common = ba & bits[b] & suffix[b]
            if common:
                c = (common & -common).bit_length() - 1
                sys.stdout.write(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()
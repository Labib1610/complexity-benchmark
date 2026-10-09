import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n + 1)]
    bits = [0] * (n + 1)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
        bits[u] |= 1 << v
        bits[v] |= 1 << u
    for i in range(1, n + 1):
        adj[i].sort()
    for a in range(1, n + 1):
        ba = bits[a]
        for b in adj[a]:
            if b <= a:
                continue
            common = ba & bits[b]
            common &= -(1 << (b + 1))
            if common:
                c = (common & -common).bit_length() - 1
                sys.stdout.write(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()
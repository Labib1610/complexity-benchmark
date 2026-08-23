import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * (n + 1)
    edges = []

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u == v:
            continue
        if u < v:
            edges.append((u, v))
        else:
            edges.append((v, u))
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)

    edges.sort()

    mask_after = [0] * (n + 1)
    full = (1 << n) - 1
    for v in range(1, n + 1):
        mask_after[v] = full & ~((1 << v) - 1)

    for u, v in edges:
        cand = adj[u] & adj[v] & mask_after[v]
        if cand:
            c = (cand & -cand).bit_length()
            sys.stdout.write(f"{u} {v} {c}\n")
            return

if __name__ == "__main__":
    solve()
import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    mask = [0] * (n + 1)
    adj = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        mask[u] |= 1 << (v - 1)
        mask[v] |= 1 << (u - 1)
        adj[u].append(v)
        adj[v].append(u)

    # Sort adjacency lists to ensure lexicographic order
    for lst in adj:
        lst.sort()

    for a in range(1, n + 1):
        for b in adj[a]:
            if b <= a:
                continue
            inter = mask[a] & mask[b]
            sub = inter >> b  # keep only nodes with index >= b
            if sub:
                lsb = sub & -sub
                p = lsb.bit_length() - 1
                c = b + p + 1
                print(a, b, c)
                return

if __name__ == "__main__":
    solve()
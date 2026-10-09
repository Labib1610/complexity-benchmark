import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    bits = [0] * (n + 1)          # 1‑based
    adj = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u == v:
            continue
        bits[u] |= 1 << (v - 1)
        bits[v] |= 1 << (u - 1)
        if u < v:
            adj[u].append(v)
            adj[v].append(u)
        else:
            adj[v].append(u)
            adj[u].append(v)

    # sort neighbour lists for deterministic order
    for lst in adj:
        lst.sort()

    all_bits = (1 << n) - 1

    for a in range(1, n + 1):
        ba = bits[a]
        for b in adj[a]:
            if b <= a:
                continue
            common = ba & bits[b]
            # keep only vertices with index > b (i.e. position >= b)
            mask = all_bits ^ ((1 << b) - 1)
            cand = common & mask
            if cand:
                # lowest set bit
                low = cand & -cand
                c = low.bit_length()          # 1‑based vertex number
                # a < b < c holds by construction
                sys.stdout.write(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()
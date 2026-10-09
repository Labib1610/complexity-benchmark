import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj_int = [0] * (n + 1)          # bitset of neighbors (1‑based vertices, bit i‑1 for vertex i)
    adj_list = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj_int[u] |= 1 << (v - 1)
        adj_int[v] |= 1 << (u - 1)
        adj_list[u].append(v)
        adj_list[v].append(u)

    for a in range(1, n + 1):
        # consider neighbors b > a in increasing order
        for b in sorted(v for v in adj_list[a] if v > a):
            intersect = adj_int[a] & adj_int[b]
            # mask out vertices <= b
            mask = (1 << b) - 1          # bits 0..b-1 (vertices 1..b)
            cand = intersect & ~mask
            if cand:
                # lowest set bit gives smallest c > b
                low_bit = cand & -cand
                c = low_bit.bit_length()   # vertex number (since bit index = c-1)
                print(a, b, c)
                return

if __name__ == "__main__":
    solve()
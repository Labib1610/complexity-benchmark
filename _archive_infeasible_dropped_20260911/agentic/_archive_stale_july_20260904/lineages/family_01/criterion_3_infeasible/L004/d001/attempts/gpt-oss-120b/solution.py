import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * (n + 1)          # bitsets, bit i means edge to i
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    # masks with bits > i set
    full_mask = (1 << (n + 1)) - 1
    higher_mask = [0] * (n + 1)
    for i in range(n + 1):
        higher_mask[i] = full_mask ^ ((1 << (i + 1)) - 1)

    # helper: index of lowest set bit (bit 0 is unused)
    def lowbit_index(x: int) -> int:
        return (x & -x).bit_length() - 1

    for a in range(1, n - 1):
        N = adj[a] & higher_mask[a]          # neighbours > a
        while N:
            b = lowbit_index(N)
            N ^= 1 << b                       # remove b
            # vertices > b that are neighbours of both a and b
            cand = adj[b] & (adj[a] & higher_mask[a]) & higher_mask[b]
            if cand:
                c = lowbit_index(cand)
                print(a, b, c)
                return

if __name__ == "__main__":
    solve()
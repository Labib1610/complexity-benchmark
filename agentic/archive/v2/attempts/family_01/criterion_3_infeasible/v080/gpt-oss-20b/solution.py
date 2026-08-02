import sys

def solve() -> None:
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adjacency_mask = [0] * (n + 1)
    adjacency_set = [set() for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adjacency_set[u].add(v)
        adjacency_set[v].add(u)
        adjacency_mask[u] |= 1 << (v - 1)
        adjacency_mask[v] |= 1 << (u - 1)

    # Precompute sorted neighbor lists where neighbor > node
    neighbor_greater = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        lst = [v for v in adjacency_set[i] if v > i]
        lst.sort()
        neighbor_greater[i] = lst

    for a in range(1, n - 1):
        mask_a = adjacency_mask[a]
        for b in neighbor_greater[a]:
            common = mask_a & adjacency_mask[b]
            mask_c = common >> b  # remove bits <= b
            if mask_c:
                # get lowest set bit position
                lowbit = mask_c & -mask_c
                pos = lowbit.bit_length() - 1
                c = b + 1 + pos
                print(a, b, c)
                return

if __name__ == "__main__":
    solve()
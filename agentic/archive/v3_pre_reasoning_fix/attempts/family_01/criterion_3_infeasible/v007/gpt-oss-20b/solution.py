import sys
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)
    adjacency = [0] * (n + 1)
    neighbors = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = next(it)
        v = next(it)
        adjacency[u] |= 1 << (v - 1)
        adjacency[v] |= 1 << (u - 1)
        neighbors[u].append(v)
        neighbors[v].append(u)
    for a in range(1, n + 1):
        neigh = neighbors[a]
        if not neigh:
            continue
        # find first neighbor > a
        i = 0
        while i < len(neigh) and neigh[i] <= a:
            i += 1
        for b in neigh[i:]:
            inter = adjacency[a] & adjacency[b]
            mask = inter >> b  # shift to discard vertices <= b
            if mask:
                lowbit = mask & -mask
                offset = lowbit.bit_length() - 1
                c = b + offset + 1
                print(a, b, c)
                return

if __name__ == "__main__":
    main()
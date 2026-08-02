import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adjacency = [[] for _ in range(n + 1)]
    adjacency_bit = [0] * (n + 1)

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adjacency[u].append(v)
        adjacency[v].append(u)
        adjacency_bit[u] |= 1 << (v - 1)
        adjacency_bit[v] |= 1 << (u - 1)

    for lst in adjacency:
        lst.sort()

    for a in range(1, n + 1):
        for b in adjacency[a]:
            if b <= a:
                continue
            # mask for bits corresponding to nodes > b
            mask = ((1 << (n - b)) - 1) << b
            inter = adjacency_bit[a] & adjacency_bit[b] & mask
            if inter:
                lowest = inter & -inter
                pos = lowest.bit_length() - 1
                c = pos + 1
                print(a, b, c)
                return

if __name__ == "__main__":
    solve()
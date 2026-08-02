import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj_bits = [0] * (n + 1)
    neighbors = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u == v:
            continue
        # set bits (zero-based)
        adj_bits[u] |= 1 << (v - 1)
        adj_bits[v] |= 1 << (u - 1)
        neighbors[u].append(v)
        neighbors[v].append(u)

    for a in range(1, n + 1):
        neigh_list = neighbors[a]
        neigh_list.sort()
        for b in neigh_list:
            if b <= a:
                continue
            common = adj_bits[a] & adj_bits[b]
            # mask bits for vertices > b
            if b < n:
                mask = ((1 << (n - b)) - 1) << b
                common &= mask
            else:
                common = 0
            if common:
                low = common & -common
                c_index = low.bit_length() - 1
                c = c_index + 1
                print(a, b, c)
                return

if __name__ == "__main__":
    solve()
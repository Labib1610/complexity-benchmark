import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m = data[0], data[1]
    adjacency_bitset = [0] * (n + 1)
    adjacency_lists = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = data[idx]
        v = data[idx + 1]
        idx += 2
        adjacency_bitset[u] |= 1 << (v - 1)
        adjacency_bitset[v] |= 1 << (u - 1)
        adjacency_lists[u].append(v)
        adjacency_lists[v].append(u)
    for i in range(1, n + 1):
        adjacency_lists[i].sort()

    for a in range(1, n + 1):
        if len(adjacency_lists[a]) == 0:
            continue
        # mask for bits corresponding to nodes > a
        mask_gt_a = ((1 << (n - a)) - 1) << a if n > a else 0
        bitsetA = adjacency_bitset[a] & mask_gt_a
        if bitsetA == 0:
            continue
        for b in adjacency_lists[a]:
            if b <= a:
                continue
            bitsetC = bitsetA & adjacency_bitset[b]
            shifted = bitsetC >> b
            if shifted:
                low_bit = (shifted & -shifted).bit_length() - 1
                c = b + low_bit + 1
                print(a, b, c)
                return

if __name__ == "__main__":
    solve()
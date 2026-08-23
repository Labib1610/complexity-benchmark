import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj_bits = [0] * (n + 1)
    ng = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj_bits[u] |= 1 << v
        adj_bits[v] |= 1 << u
        if u < v:
            ng[u].append(v)
        else:
            ng[v].append(u)

    for i in range(1, n + 1):
        ng[i].sort()

    mask_gt = [0] * (n + 1)
    for i in range(1, n + 1):
        mask_gt[i] = -1 << (i + 1)

    out = sys.stdout.write
    for a in range(1, n + 1):
        ab = adj_bits[a]
        for b in ng[a]:
            common = ab & adj_bits[b]
            if common:
                common &= mask_gt[b]
                if common:
                    c = (common & -common).bit_length() - 1
                    out(f"{a} {b} {c}\n")
                    return

if __name__ == "__main__":
    solve()
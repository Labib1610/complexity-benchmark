import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj_mask = [0] * n               # bitset per vertex
    adj_list = [[] for _ in range(n)]

    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        # set bits
        adj_mask[u] |= 1 << v
        adj_mask[v] |= 1 << u
        adj_list[u].append(v)
        adj_list[v].append(u)

    # sort adjacency lists for deterministic order
    for lst in adj_list:
        lst.sort()

    for a in range(n):
        mask_a = adj_mask[a]
        for b in adj_list[a]:
            if b <= a:
                continue
            common = mask_a & adj_mask[b]
            # discard vertices <= b
            t = common >> (b + 1)
            if t:
                low = (t & -t).bit_length() - 1
                c = b + 1 + low
                # output 1‑based
                sys.stdout.write(f"{a+1} {b+1} {c+1}")
                return

if __name__ == "__main__":
    solve()
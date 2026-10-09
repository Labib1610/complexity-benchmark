import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj_int = [0] * (n + 1)          # 1‑based
    adj_list = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        # set bits (0‑based inside the int)
        adj_int[u] |= 1 << (v - 1)
        adj_int[v] |= 1 << (u - 1)
        adj_list[u].append(v)
        adj_list[v].append(u)

    # sort neighbour lists for increasing order iteration
    for lst in adj_list:
        lst.sort()

    for a in range(1, n - 1):
        a_bits = adj_int[a]
        for b in adj_list[a]:
            if b <= a:
                continue
            # neighbours common to a and b
            common = a_bits & adj_int[b]
            # keep only vertices > b
            mask = ~((1 << b) - 1)          # bits b+1 .. n are 1
            common &= mask
            if common:
                # lowest set bit gives smallest c
                lowest = common & -common
                c = lowest.bit_length()     # 1‑based index
                # output in ascending order (already a<b<c)
                sys.stdout.write(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()
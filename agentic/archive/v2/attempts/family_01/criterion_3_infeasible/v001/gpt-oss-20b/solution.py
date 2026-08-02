import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)

    # 1‑based vertices
    adj_bit = [0] * (n + 1)           # bitsets
    adj_list = [[] for _ in range(n + 1)]  # neighbour lists

    for _ in range(m):
        u = next(it)
        v = next(it)
        if u == v:
            continue            # ignore self loops, if any
        # set bits (vertices are 1‑based)
        adj_bit[u] |= 1 << (v - 1)
        adj_bit[v] |= 1 << (u - 1)
        adj_list[u].append(v)
        adj_list[v].append(u)

    # sort neighbour lists
    for lst in adj_list:
        lst.sort()

    # search the smallest triangle
    for a in range(1, n + 1):
        bit_a = adj_bit[a]
        for b in adj_list[a]:
            if b <= a:
                continue          # only a < b
            # common neighbours of a and b
            common = bit_a & adj_bit[b]
            if common == 0:
                continue
            # we need a neighbour > b
            shifted = common >> b
            if shifted == 0:
                continue
            # least significant set bit of shifted
            # pos = index of that bit
            pos = (shifted & -shifted).bit_length() - 1
            c = b + pos + 1
            # output the triangle
            sys.stdout.write(f"{a} {b} {c}\n")
            return

if __name__ == "__main__":
    solve()
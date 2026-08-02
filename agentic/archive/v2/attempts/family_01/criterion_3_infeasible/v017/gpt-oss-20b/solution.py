import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj_mask = [0] * n
    adj_list = [[] for _ in range(n)]

    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj_mask[u] |= 1 << v
        adj_mask[v] |= 1 << u
        adj_list[u].append(v)
        adj_list[v].append(u)

    for lst in adj_list:
        lst.sort()

    for a in range(n):
        for b in adj_list[a]:
            if b <= a:
                continue
            common = adj_mask[a] & adj_mask[b]
            # mask bits > b
            mask = common & ~((1 << (b + 1)) - 1)
            if mask:
                # lowest set bit
                low = mask & -mask
                c = low.bit_length() - 1
                # output 1‑based indices
                print(a + 1, b + 1, c + 1)
                return

if __name__ == "__main__":
    solve()
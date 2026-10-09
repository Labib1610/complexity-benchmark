import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)

    adj_bit = [0] * n
    adj_list = [[] for _ in range(n)]

    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        adj_bit[u] |= 1 << v
        adj_bit[v] |= 1 << u
        adj_list[u].append(v)
        adj_list[v].append(u)

    for lst in adj_list:
        lst.sort()

    for a in range(n):
        a_bits = adj_bit[a]
        for b in adj_list[a]:
            if b <= a:
                continue
            common = a_bits & adj_bit[b]
            # delete vertices <= b
            mask = (1 << (b + 1)) - 1
            common &= ~mask
            if common:
                low = common & -common          # lowest set bit
                c = low.bit_length() - 1
                # output 1‑based indices
                sys.stdout.write(f"{a+1} {b+1} {c+1}")
                return

if __name__ == "__main__":
    solve()
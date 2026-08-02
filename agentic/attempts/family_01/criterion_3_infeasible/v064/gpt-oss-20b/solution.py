import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)

    adj_list = [[] for _ in range(n + 1)]
    adj_bit = [0] * (n + 1)

    for _ in range(m):
        u = next(it)
        v = next(it)
        adj_list[u].append(v)
        adj_list[v].append(u)
        adj_bit[u] |= 1 << v
        adj_bit[v] |= 1 << u

    for lst in adj_list:
        lst.sort()

    for a in range(1, n + 1):
        bits_a = adj_bit[a]
        for b in adj_list[a]:
            if b <= a:
                continue
            inter = bits_a & adj_bit[b]
            shifted = inter >> b  # drop bits 1..b
            if shifted:
                low = shifted & -shifted
                c = (low.bit_length() - 1) + b
                print(a, b, c)
                return

if __name__ == "__main__":
    solve()
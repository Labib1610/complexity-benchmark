import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)

    adj_bits = [0] * (n + 1)
    adj_list = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = next(it)
        v = next(it)
        bit_u = 1 << (v - 1)
        bit_v = 1 << (u - 1)
        adj_bits[u] |= bit_u
        adj_bits[v] |= bit_v
        adj_list[u].append(v)
        adj_list[v].append(u)

    for i in range(1, n + 1):
        adj_list[i].sort()

    for a in range(1, n - 1):
        bits_a = adj_bits[a]
        for b in adj_list[a]:
            if b <= a:
                continue
            inter = bits_a & adj_bits[b]
            # keep only neighbors with index >= b (node number > b)
            inter_shift = inter >> b
            if inter_shift:
                low = inter_shift & -inter_shift
                pos = low.bit_length() - 1  # 0‑based position after shift
                c = pos + b + 1
                print(a, b, c)
                return

if __name__ == "__main__":
    solve()
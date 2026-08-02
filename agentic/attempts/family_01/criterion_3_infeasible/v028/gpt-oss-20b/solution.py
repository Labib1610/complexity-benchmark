import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)

    adj_bit = [0] * (n + 1)
    adj_list = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = next(it)
        v = next(it)
        adj_bit[u] |= 1 << (v - 1)
        adj_bit[v] |= 1 << (u - 1)
        adj_list[u].append(v)
        adj_list[v].append(u)

    for i in range(1, n + 1):
        adj_list[i].sort()

    for a in range(1, n + 1):
        for b in adj_list[a]:
            if b <= a:
                continue
            inter = adj_bit[a] & adj_bit[b]
            inter_shift = inter >> b
            if inter_shift:
                lsb = inter_shift & -inter_shift
                pos = lsb.bit_length() - 1
                c = b + pos + 1
                sys.stdout.write(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()
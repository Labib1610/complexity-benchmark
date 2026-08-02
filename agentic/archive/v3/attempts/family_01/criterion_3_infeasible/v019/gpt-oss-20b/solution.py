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
        if u == v:
            continue
        bit_u = 1 << (v - 1)
        bit_v = 1 << (u - 1)
        adj_bit[u] |= bit_u
        adj_bit[v] |= bit_v
        adj_list[u].append(v)
        adj_list[v].append(u)

    for lst in adj_list:
        lst.sort()

    all_ones = (1 << n) - 1

    for a in range(1, n + 1):
        for b in adj_list[a]:
            if b <= a:
                continue
            common = adj_bit[a] & adj_bit[b]
            mask = all_ones & ~((1 << b) - 1)  # bits for nodes > b
            common_masked = common & mask
            if common_masked:
                c_bit = common_masked & -common_masked
                c = c_bit.bit_length()
                sys.stdout.write(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()
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

    for lst in adj_list:
        lst.sort()

    for a in range(1, n - 1):
        bits_a = adj_bits[a]
        for b in adj_list[a]:
            if b <= a:
                continue
            intersection = bits_a & adj_bits[b]
            mask = intersection >> b
            if mask:
                lowbit = mask & -mask
                tz = lowbit.bit_length() - 1
                c = b + 1 + tz
                sys.stdout.write(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()
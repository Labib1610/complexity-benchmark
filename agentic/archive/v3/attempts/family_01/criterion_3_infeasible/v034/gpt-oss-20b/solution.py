import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m = data[0], data[1]
    adj_bits = [0] * (n + 1)
    adj_list = [[] for _ in range(n + 1)]

    idx = 2
    for _ in range(m):
        u = data[idx]
        v = data[idx + 1]
        idx += 2
        bit_u = 1 << (v - 1)
        bit_v = 1 << (u - 1)
        adj_bits[u] |= bit_u
        adj_bits[v] |= bit_v
        adj_list[u].append(v)
        adj_list[v].append(u)

    for lst in adj_list:
        lst.sort()

    out = []
    for a in range(1, n + 1):
        for b in adj_list[a]:
            if b <= a:
                continue
            common = adj_bits[a] & adj_bits[b]
            shifted = common >> b
            if shifted:
                lsb = shifted & -shifted
                offset = lsb.bit_length() - 1
                c = b + offset + 1
                if c <= n:
                    sys.stdout.write(f"{a} {b} {c}")
                    return

if __name__ == "__main__":
    solve()
import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj_bits = [0] * (n + 1)
    adj_list = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        # set bits (0‑based)
        adj_bits[u] |= 1 << (v - 1)
        adj_bits[v] |= 1 << (u - 1)
        adj_list[u].append(v)
        adj_list[v].append(u)

    for lst in adj_list:
        lst.sort()

    out = []
    for a in range(1, n + 1):
        bits_a = adj_bits[a]
        for b in adj_list[a]:
            if b <= a:
                continue
            common = bits_a & adj_bits[b]
            mask = common >> b          # keep only vertices > b
            if mask:
                low = mask & -mask
                pos = low.bit_length() - 1
                c = b + 1 + pos
                out = [a, b, c]
                sys.stdout.write(f"{a} {b} {c}\n")
                return

if __name__ == "__main__":
    solve()
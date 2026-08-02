import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj_bit = [0] * (n + 1)
    adj_list = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj_bit[u] |= 1 << (v - 1)
        adj_bit[v] |= 1 << (u - 1)
        adj_list[u].append(v)
        adj_list[v].append(u)

    for a in range(1, n + 1):
        adj_list[a].sort()
        for b in adj_list[a]:
            if b <= a:
                continue
            inter = adj_bit[a] & adj_bit[b]
            mask = inter >> b  # shift to remove bits <= b
            if mask:
                lsb = mask & -mask
                offset = lsb.bit_length() - 1
                c = b + 1 + offset
                sys.stdout.write(f"{a} {b} {c}\n")
                return

if __name__ == "__main__":
    solve()
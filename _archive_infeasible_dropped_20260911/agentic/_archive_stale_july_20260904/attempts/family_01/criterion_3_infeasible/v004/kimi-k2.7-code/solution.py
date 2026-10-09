import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)

    adj_bits = [0] * n
    adj_list = [[] for _ in range(n)]

    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        adj_bits[u] |= 1 << v
        adj_bits[v] |= 1 << u
        adj_list[u].append(v)
        adj_list[v].append(u)

    for i in range(n):
        adj_list[i].sort()

    for a in range(n):
        for b in adj_list[a]:
            if b <= a:
                continue
            common = adj_bits[a] & adj_bits[b]
            mask = ~((1 << (b + 1)) - 1)
            cand = common & mask
            if cand:
                lsb = cand & -cand
                c = lsb.bit_length() - 1
                sys.stdout.write(f"{a + 1} {b + 1} {c + 1}\n")
                return

if __name__ == "__main__":
    solve()
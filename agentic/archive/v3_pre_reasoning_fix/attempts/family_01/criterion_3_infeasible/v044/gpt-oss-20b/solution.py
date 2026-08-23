import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj_bits = [0] * n
    adj_list = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj_bits[u] |= 1 << v
        adj_bits[v] |= 1 << u
        adj_list[u].append(v)
        adj_list[v].append(u)

    for a in range(n):
        for b in adj_list[a]:
            if b <= a:
                continue
            inter = adj_bits[a] & adj_bits[b]
            mask = inter >> (b + 1)
            if mask == 0:
                continue
            lsb = mask & -mask
            t = lsb.bit_length() - 1
            c = b + 1 + t
            print(a + 1, b + 1, c + 1)
            return

if __name__ == "__main__":
    solve()
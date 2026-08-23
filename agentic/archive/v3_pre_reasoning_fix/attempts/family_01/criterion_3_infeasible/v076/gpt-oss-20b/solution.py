import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
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
            common = adj_bits[a] & adj_bits[b]
            mask = common >> (b + 1)          # remove bits <= b
            if mask:
                lowbit = mask & -mask          # lowest set bit
                c = (b + 1) + (lowbit.bit_length() - 1)
                print(a + 1, b + 1, c + 1)
                return

if __name__ == "__main__":
    solve()
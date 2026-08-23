import sys

def solve():
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
    for i in range(n):
        adj_list[i].sort()
    for a in range(n):
        abits = adj_bits[a]
        for b in adj_list[a]:
            if b <= a:
                continue
            inter = abits & adj_bits[b]
            if inter:
                mask = (inter >> (b + 1)) << (b + 1)
                if mask:
                    c = (mask & -mask).bit_length() - 1
                    sys.stdout.write(f"{a + 1} {b + 1} {c + 1}")
                    return

if __name__ == "__main__":
    solve()
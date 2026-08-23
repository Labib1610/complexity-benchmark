import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * (n + 1)  # 1-indexed, bit i corresponds to vertex i+1
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)

    for a in range(1, n - 1):
        a_mask = adj[a]
        for b in range(a + 1, n):
            if not (a_mask >> (b - 1)) & 1:
                continue
            inter = a_mask & adj[b]
            # mask bits for vertices > b
            mask = ((1 << (n - b)) - 1) << b
            inter &= mask
            if inter:
                lsb = inter & -inter
                c_idx = lsb.bit_length() - 1
                c = c_idx + 1
                sys.stdout.write(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()
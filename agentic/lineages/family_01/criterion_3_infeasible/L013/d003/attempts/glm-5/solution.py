import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    idx = 2
    adj = [0] * (n + 1)
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx+1]); idx += 2
        if u > v:
            u, v = v, u
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
    
    full = (1 << (n + 1)) - 1
    for a in range(1, n - 1):
        adj_a = adj[a]
        if adj_a == 0:
            continue
        # candidates b > a with edge a-b
        candidates = []
        b = a + 1
        while b <= n:
            if (adj_a >> b) & 1:
                candidates.append(b)
            b += 1
        for b in candidates:
            common = adj_a & adj[b]
            # keep only bits > b
            common &= full & ~((1 << (b + 1)) - 1)
            if common:
                c = (common & -common).bit_length() - 1
                print(a, b, c)
                return

if __name__ == "__main__":
    solve()
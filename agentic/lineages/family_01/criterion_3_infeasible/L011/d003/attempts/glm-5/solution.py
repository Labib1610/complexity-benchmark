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
    
    best = None
    best_trace = -1
    for a in range(1, n + 1):
        adj_a = adj[a]
        if adj_a == 0:
            continue
        b = a + 1
        while b <= n:
            if (adj_a >> b) & 1:
                common = adj_a & adj[b]
                while common:
                    c_bit = common & (-common)
                    c = c_bit.bit_length() - 1
                    if c > b:
                        trace = a * 100000000 + b * 10000 + c
                        if best is None or trace < best_trace:
                            best = (a, b, c)
                            best_trace = trace
                    common ^= c_bit
            b += 1
    if best is not None:
        sys.stdout.write(f"{best[0]} {best[1]} {best[2]}\n")

solve()
import sys

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [0] * (n + 1)
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u] |= (1 << (v - 1))
        adj[v] |= (1 << (u - 1))
    
    best = None
    best_trace = None
    
    # Iterate over edges
    for u in range(1, n + 1):
        for v in range(u + 1, n + 1):
            if (adj[u] >> (v - 1)) & 1:
                # common neighbors > v
                common = adj[u] & adj[v]
                # mask out nodes <= v
                mask = ((1 << n) - 1) ^ ((1 << v) - 1)
                common &= mask
                while common:
                    # get lowest set bit
                    lsb = common & -common
                    w = lsb.bit_length()  # 1-indexed
                    trace = u * 10**8 + v * 10**4 + w
                    if best_trace is None or trace < best_trace:
                        best_trace = trace
                        best = (u, v, w)
                    common ^= lsb
    
    print(*best)

if __name__ == "__main__":
    main()
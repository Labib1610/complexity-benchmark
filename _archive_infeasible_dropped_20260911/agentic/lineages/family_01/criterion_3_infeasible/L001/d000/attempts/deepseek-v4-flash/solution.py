import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    # adjacency matrix as bitsets (Python integers)
    adj = [0] * (n + 1)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
    
    # Try all possible a, then b, then c
    for a in range(1, n + 1):
        # candidates for b: neighbors of a with index > a
        b_mask = adj[a] & ~((1 << (a + 1)) - 1)  # keep only > a
        while b_mask:
            # get lowest set bit
            lsb = b_mask & -b_mask
            b = lsb.bit_length() - 1
            b_mask ^= lsb
            
            # candidates for c: neighbors of both a and b, with index > b
            c_mask = adj[a] & adj[b] & ~((1 << (b + 1)) - 1)
            if c_mask:
                lsb_c = c_mask & -c_mask
                c = lsb_c.bit_length() - 1
                print(a, b, c)
                return

if __name__ == "__main__":
    solve()
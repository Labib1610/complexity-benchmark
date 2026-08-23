import sys

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    
    adj = [0] * (n + 1)  # adj[v] is a bitmask of neighbors
    
    for _ in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
    
    for a in range(1, n + 1):
        # neighbors of a that are > a
        mask_a = adj[a] & ~((1 << (a + 1)) - 1)  # bits > a
        # iterate b in increasing order
        b = a + 1
        while b <= n and mask_a:
            if not (mask_a >> b) & 1:
                b += 1
                continue
            # look for c > b in mask_a that is also neighbor of b
            mask_b = adj[b] & mask_a & ~((1 << (b + 1)) - 1)
            if mask_b:
                # find lowest set bit = smallest c
                c = (mask_b & -mask_b).bit_length() - 1
                print(f"{a} {b} {c}")
                return
            b += 1
    
    # Should not reach here per problem guarantee
    print("-1 -1 -1")

solve()
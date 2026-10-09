import sys

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    
    adj = [0] * (n + 1)
    for _ in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        if u > v:
            u, v = v, u
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
    
    for a in range(1, n + 1):
        neighbors_a = adj[a]
        b = a + 1
        while b <= n:
            if (neighbors_a >> b) & 1:
                # Find c > b where c is neighbor of both a and b
                common = neighbors_a & adj[b]
                # Mask to keep only bits > b
                mask = ~((1 << (b + 1)) - 1)
                common &= mask
                if common:
                    # Find lowest set bit
                    c = (common & -common).bit_length() - 1
                    print(f"{a} {b} {c}")
                    return
            b += 1
    
    # Should not reach here per problem guarantee
    print("-1")

solve()
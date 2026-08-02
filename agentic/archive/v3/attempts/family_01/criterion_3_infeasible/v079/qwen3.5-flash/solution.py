import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)

def solve():
    # Read all input from standard input
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
    
    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return
    
    # Adjacency list for iterating neighbors in sorted order
    adj = [[] for _ in range(n)]
    # Adjacency bitmask for fast intersection
    adj_mask = [0] * n
    
    # Read m edges
    for _ in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        
        adj[u].append(v)
        adj[v].append(u)
        
        adj_mask[u] |= (1 << v)
        adj_mask[v] |= (1 << u)
    
    # Sort adjacency lists to ensure we visit neighbors in increasing order
    for i in range(n):
        adj[i].sort()
    
    # Precompute mask_gt[i] which has bits i+1 to n-1 set.
    # mask_gt[i] = (1 << n) - (1 << (i + 1))
    # We compute (1 << n) once
    limit_mask = 1 << n
    
    mask_gt = [0] * n
    for i in range(n):
        mask_gt[i] = limit_mask - (1 << (i + 1))
    
    # Iterate to find the lexicographically smallest triangle (a, b, c) with a < b < c
    # Since we want lexicographically smallest, we iterate a from 0 to n-1.
    # For a fixed a, we iterate b from neighbors of a such that b > a.
    # Since adj[a] is sorted, b is visited in increasing order.
    # For a fixed pair (a, b), we need the smallest c > b such that c is a common neighbor.
    
    for a in range(n):
        for b in adj[a]:
            if b > a:
                # We need to find c > b such that c is connected to both a and b.
                # Common neighbors of a and b are given by adj_mask[a] & adj_mask[b].
                common = adj_mask[a] & adj_mask[b]
                
                # We only care about c > b.
                # mask_gt[b] has bits set for all indices > b.
                # valid will have bits set for common neighbors > b.
                valid = common & mask_gt[b]
                
                if valid:
                    # If valid is non-zero, there exists at least one such c.
                    # We want the smallest c, which corresponds to the lowest set bit.
                    lsb = valid & -valid
                    c = lsb.bit_length() - 1
                    
                    # Output 1-based indices
                    print(f"{a+1} {b+1} {c+1}")
                    return

if __name__ == '__main__':
    solve()
import sys

def solve():
    # Read all input from standard input efficiently
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
    
    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return
    
    # Adjacency bitmasks
    # adj[u] will have the v-th bit set if u and v are connected
    # We use 1-based indexing for nodes, so bit k corresponds to node k
    adj = [0] * (n + 1)
    
    # Adjacency lists for iteration order
    adj_list = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
        
        adj_list[u].append(v)
        adj_list[v].append(u)
        
    # Precompute masks to clear bits <= v
    # masks[i] will be an integer with bits 0 to i set
    # This helps in clearing bits corresponding to nodes <= v efficiently
    masks = [0] * (n + 2)
    current_mask = 0
    for i in range(n + 2):
        current_mask |= (1 << i)
        masks[i] = current_mask
        
    # Sort neighbors to ensure we process v in increasing order (lexicographical requirement)
    for i in range(1, n + 1):
        adj_list[i].sort()
        
    # Iterate u from 1 to n
    for u in range(1, n + 1):
        # Iterate v from neighbors of u
        for v in adj_list[u]:
            if v <= u:
                continue
            
            # If edge (u, v) exists (it must, since v in adj_list[u])
            # Check for common neighbors w
            # We want smallest w such that w > v
            
            common = adj[u] & adj[v]
            
            # Clear bits 0..v. masks[v] has bits 0..v set.
            # So ~masks[v] has 0s at 0..v.
            # This ensures any remaining bit w corresponds to w > v.
            common &= ~masks[v]
            
            if common:
                # Find the smallest set bit index
                # common & -common isolates the lowest set bit
                lsb = common & -common
                
                # The bit index k satisfies 2^k = lsb.
                # bit_length() of 2^k is k + 1.
                w = lsb.bit_length() - 1
                
                # Output the result
                print(f"{u} {v} {w}")
                return

if __name__ == '__main__':
    solve()
import sys

# Increase recursion depth just in case, though not needed for this iterative solution
sys.setrecursionlimit(2000)

def solve():
    # Read all input from stdin efficiently
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Adjacency bitmasks and lists
    # Workers are 1-indexed, so size n + 1
    # adj[i] will store a bitmask where the k-th bit is set if worker k is a neighbor of i
    adj = [0] * (n + 1)
    adj_list = [[] for _ in range(n + 1)]
    
    # Parse edges
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        
        # Update bitmask
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
        
        # Update adjacency list
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    # Sort adjacency lists to ensure we iterate b in increasing order
    # This is crucial for finding the lexicographically smallest triplet
    for i in range(1, n + 1):
        adj_list[i].sort()
    
    # Iterate to find the lexicographically smallest triplet (a, b, c)
    # Condition: a < b < c and edges (a,b), (a,c), (b,c) exist.
    # We want to minimize a, then b, then c.
    for a in range(1, n + 1):
        # We only need to check neighbors b of a where b > a.
        # Since adj_list[a] is sorted, we can iterate and skip b <= a.
        for b in adj_list[a]:
            if b <= a:
                continue
            
            # We have edge (a, b). Now find c > b such that (a, c) and (b, c) are edges.
            # This is equivalent to finding the smallest bit set in (adj[a] & adj[b]) that is > b.
            
            common = adj[a] & adj[b]
            
            # Mask out bits <= b. 
            # We want bits corresponding to workers c where c > b.
            # Bit k corresponds to worker k.
            # So we want to keep bits at positions b+1, b+2, ..., n.
            # We clear bits 0 to b.
            # Mask for bits 0 to b is (1 << (b + 1)) - 1.
            # We invert this mask to clear those bits.
            
            mask = (1 << (b + 1)) - 1
            common &= ~mask
            
            if common:
                # Find the lowest set bit index.
                # common & -common isolates the lowest set bit.
                # bit_length() gives the position of the highest bit + 1.
                # For a power of 2 (2^k), bit_length() is k + 1.
                # So k = bit_length() - 1.
                c = (common & -common).bit_length() - 1
                
                print(f"{a} {b} {c}")
                return

if __name__ == '__main__':
    solve()
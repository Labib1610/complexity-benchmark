import sys

# Increase recursion depth just in case, though not strictly needed here
sys.setrecursionlimit(2000)

def main():
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

    # Adjacency list and adjacency masks
    # IDs are 1-based, so we use size n + 1
    # adj[i] stores neighbors of i
    adj = [[] for _ in range(n + 1)]
    # adj_mask[i] stores a bitmask where the k-th bit is 1 if k is a neighbor of i
    adj_mask = [0] * (n + 1)
    
    # Read m edges
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        
        adj[u].append(v)
        adj[v].append(u)
        
        # Set bit v in mask of u, and bit u in mask of v
        # Using 1 << k sets the k-th bit (0-indexed), which corresponds to ID k
        adj_mask[u] |= (1 << v)
        adj_mask[v] |= (1 << u)
        
    # Sort adjacency lists to ensure we iterate neighbors in increasing order
    # This helps in finding the lexicographically smallest triple
    for i in range(1, n + 1):
        adj[i].sort()
        
    # Iterate to find the lexicographically smallest triple (a, b, c)
    # We want to minimize a, then b, then c.
    # Iterate a from 1 to n
    for a in range(1, n + 1):
        # Iterate neighbors b of a
        # We only care about b > a to maintain a < b < c condition
        # and to avoid duplicate checks.
        # Since adj[a] is sorted, we encounter smaller b first.
        for b in adj[a]:
            if b <= a:
                continue
            
            # Check if there exists a c > b such that c is connected to both a and b.
            # Common neighbors of a and b are given by the intersection of their adjacency masks.
            common = adj_mask[a] & adj_mask[b]
            
            # We need c > b.
            # Create a mask that has 0s at positions 0 to b, and 1s elsewhere.
            # (1 << (b + 1)) - 1 creates a mask with 1s at 0..b.
            # ~((1 << (b + 1)) - 1) inverts it.
            # Note: Python integers are arbitrary precision, so ~x is -x-1 which behaves like infinite 1s.
            # ANDing with common (which is positive and finite) works correctly.
            
            c_mask = common & ~((1 << (b + 1)) - 1)
            
            if c_mask:
                # If c_mask is non-zero, there is at least one common neighbor > b.
                # We need the smallest such c.
                # The smallest set bit corresponds to the smallest c.
                # (c_mask & -c_mask) isolates the lowest set bit.
                # .bit_length() - 1 gives the index of that bit.
                c = (c_mask & -c_mask).bit_length() - 1
                print(a, b, c)
                return

if __name__ == '__main__':
    main()
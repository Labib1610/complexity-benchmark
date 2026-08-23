import sys

# Increase recursion depth just in case (though not strictly needed here)
sys.setrecursionlimit(2000)

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Adjacency bitmasks for O(1) edge checks and set operations
    adj = [0] * n
    # Adjacency lists to iterate over neighbors
    adj_list = [[] for _ in range(n)]
    
    # Read edges
    for _ in range(m):
        try:
            u = int(next(iterator)) - 1
            v = int(next(iterator)) - 1
            adj[u] |= (1 << v)
            adj[v] |= (1 << u)
            adj_list[u].append(v)
            adj_list[v].append(u)
        except StopIteration:
            break
            
    # Sort adjacency lists to ensure we process neighbors in increasing order.
    # This is crucial for finding the lexicographically smallest triple.
    for i in range(n):
        adj_list[i].sort()
        
    # Iterate to find the lexicographically smallest triangle (a, b, c)
    # with 1 <= a < b < c <= n.
    # We iterate a from 0 to n-1 (corresponding to 1 to n).
    for a in range(n):
        # Iterate b in neighbors of a.
        # Since adj_list is sorted, we process b in increasing order.
        # We only consider b > a to satisfy the ordering constraint.
        for b in adj_list[a]:
            if b <= a:
                continue
            
            # We have edge (a, b).
            # We need to find a neighbor c of both a and b such that c > b.
            # Intersection of neighbors of a and b:
            common = adj[a] & adj[b]
            
            # We need bits in common that are > b.
            # Mask out bits 0 to b.
            # (1 << (b + 1)) - 1 creates a mask with bits 0..b set to 1.
            # ~(...) inverts it, clearing bits 0..b (leaving bits b+1 and higher as 1).
            mask = common & ~((1 << (b + 1)) - 1)
            
            if mask:
                # Find the lowest set bit in mask.
                # (mask & -mask) extracts the lowest set bit as a power of 2.
                # .bit_length() - 1 gives the index of that bit.
                # Since mask only has bits > b, this c will satisfy c > b.
                c = (mask & -mask).bit_length() - 1
                
                # Found the lexicographically smallest triple (a, b, c)
                # Output 1-based indices
                print(f"{a + 1} {b + 1} {c + 1}")
                return

if __name__ == '__main__':
    solve()
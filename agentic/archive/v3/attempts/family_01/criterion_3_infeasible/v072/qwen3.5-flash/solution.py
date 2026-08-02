import sys

# Increase recursion depth just in case, though not used here
sys.setrecursionlimit(2000)

def solve():
    # Read all input from standard input at once
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Adjacency masks for fast intersection checks
    # We use 1-based indexing for vertices to match the problem statement directly
    # adj_mask[u] will have the v-th bit set if there is an edge between u and v
    adj_mask = [0] * (n + 1)
    
    # Adjacency lists to iterate neighbors in sorted order
    adj_list = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        
        # Set bits in masks
        adj_mask[u] |= (1 << v)
        adj_mask[v] |= (1 << u)
        
        # Add to adjacency lists
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    # Sort adjacency lists to ensure we check b in increasing order
    # This is crucial for finding the lexicographically smallest triangle
    for i in range(1, n + 1):
        adj_list[i].sort()
        
    # Iterate through each vertex a
    for a in range(1, n + 1):
        # Iterate through neighbors b of a
        # We look for triangles (a, b, c) with a < b < c
        for b in adj_list[a]:
            if b <= a:
                continue
            
            # Check for common neighbors c > b
            # common neighbors are in (adj_mask[a] & adj_mask[b])
            common = adj_mask[a] & adj_mask[b]
            
            # We need the smallest c such that c > b.
            # In common, bits represent vertices. We want smallest set bit index > b.
            # Shift common right by (b + 1) to discard bits <= b.
            # The lowest set bit of the result corresponds to the smallest valid c.
            cand = common >> (b + 1)
            
            if cand > 0:
                # Find the index of the lowest set bit of cand
                # (cand & -cand) isolates the lowest set bit
                lsb = cand & -cand
                # bit_length() returns the number of bits required to represent an integer
                # For a power of 2, it returns the index + 1
                k = lsb.bit_length() - 1
                
                # The actual vertex index c
                c = b + 1 + k
                
                # We found the lexicographically smallest triangle (a, b, c)
                # Since we iterate a increasing, then b increasing, then find smallest c,
                # the first one found is the answer.
                print(f"{a} {b} {c}")
                return

if __name__ == '__main__':
    solve()
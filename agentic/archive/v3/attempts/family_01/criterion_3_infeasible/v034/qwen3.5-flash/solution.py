import sys

# Increase recursion depth just in case, though not needed here
sys.setrecursionlimit(2000)

def solve():
    # Read all input from stdin
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Adjacency mask for fast intersection using bit manipulation
    # Vertices are 1-indexed. We will use bit positions 1 to n.
    # adj_mask[u] has the v-th bit set if there is an edge between u and v.
    adj_mask = [0] * (n + 1)
    
    # Adjacency list to iterate neighbors in order
    adj_list = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
            
            # Set bits in masks
            adj_mask[u] |= (1 << v)
            adj_mask[v] |= (1 << u)
            
            adj_list[u].append(v)
            adj_list[v].append(u)
        except StopIteration:
            break
    
    # Sort adjacency lists and remove duplicates to ensure iteration order and efficiency
    for i in range(1, n + 1):
        adj_list[i] = sorted(list(set(adj_list[i])))
        
    # Iterate to find the lexicographically smallest triangle
    # We want the triple (a, b, c) with a < b < c such that all pairs are connected.
    # We iterate 'a' from 1 to n to minimize 'a'.
    # For a fixed 'a', we iterate 'b' from neighbors of 'a' with b > a (sorted order) to minimize 'b'.
    # For fixed 'a' and 'b', we find the smallest 'c' > b such that (a, c) and (b, c) are edges.
    
    for a in range(1, n + 1):
        # We only care about neighbors b > a
        for b in adj_list[a]:
            if b <= a:
                continue
            
            # We need to find smallest c > b such that (a, c) and (b, c) are edges.
            # This corresponds to finding the smallest bit set in (adj_mask[a] & adj_mask[b])
            # that is > b.
            
            common = adj_mask[a] & adj_mask[b]
            
            # We want to ignore bits <= b.
            # Create a mask with bits 0..b set to 1.
            # Then invert it to get bits 0..b as 0, others as 1.
            # (1 << (b + 1)) - 1 creates a mask with bits 0 to b set to 1.
            mask_le_b = (1 << (b + 1)) - 1
            common_filtered = common & ~mask_le_b
            
            if common_filtered:
                # Find the lowest set bit
                # common_filtered & -common_filtered isolates the lowest set bit
                # .bit_length() - 1 gives the index of that bit
                c = (common_filtered & -common_filtered).bit_length() - 1
                
                # Since we iterate a, then b (in increasing order), and find smallest c,
                # the first triangle we find is the lexicographically smallest.
                print(f"{a} {b} {c}")
                return

if __name__ == '__main__':
    solve()
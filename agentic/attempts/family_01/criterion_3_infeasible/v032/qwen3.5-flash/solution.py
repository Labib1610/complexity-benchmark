import sys

# Increase recursion depth just in case, though not strictly needed here.
sys.setrecursionlimit(2000)

def solve():
    # Read all input from standard input at once for efficiency
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
    
    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Adjacency bitmask: adj_mask[u] has the v-th bit set if u is connected to v.
    # Indices are 1-based, so we need size n + 1.
    # Python integers support arbitrary precision, so they act as bitsets.
    adj_mask = [0] * (n + 1)
    
    # Adjacency list: adj_list[u] contains the list of neighbors of u.
    # We will sort this later to ensure we process neighbors in increasing order.
    adj_list = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        
        # Update bitmask
        adj_mask[u] |= (1 << v)
        adj_mask[v] |= (1 << u)
        
        # Update adjacency list
        adj_list[u].append(v)
        adj_list[v].append(u)
        
    # Sort adjacency lists to iterate neighbors in increasing order.
    # Also remove duplicates if any (though problem implies simple graph usually).
    for i in range(1, n + 1):
        adj_list[i] = sorted(list(set(adj_list[i])))

    # Iterate through each node 'a' from 1 to n.
    # We want to find the lexicographically smallest triple (a, b, c) with a < b < c.
    for a in range(1, n + 1):
        # Iterate through neighbors 'b' of 'a'.
        # Since adj_list[a] is sorted, we encounter smaller 'b' first.
        for b in adj_list[a]:
            # We need a < b < c, so we must have b > a.
            if b <= a:
                continue
            
            # We need to find a 'c' such that c is connected to both 'a' and 'b',
            # and c > b.
            # We can find common neighbors of 'a' and 'b' using bitwise intersection.
            common = adj_mask[a] & adj_mask[b]
            
            # We are interested in 'c' > b.
            # We shift 'common' right by (b + 1) bits.
            # The bit at position 'c' (where c > b) will be moved to position 'c - (b + 1)'.
            # If the result is non-zero, the lowest set bit corresponds to the smallest 'c' > b.
            shifted = common >> (b + 1)
            
            if shifted:
                # (shifted & -shifted) isolates the lowest set bit.
                # .bit_length() - 1 gives the 0-based index of that bit.
                lsb_index = (shifted & -shifted).bit_length() - 1
                
                # Reconstruct the original index 'c'
                c = lsb_index + b + 1
                
                # We found the smallest valid 'c' for the current 'a' and 'b'.
                # Since we iterate 'a' then 'b' in increasing order, this is the
                # lexicographically smallest triple.
                print(f"{a} {b} {c}")
                return

if __name__ == '__main__':
    solve()
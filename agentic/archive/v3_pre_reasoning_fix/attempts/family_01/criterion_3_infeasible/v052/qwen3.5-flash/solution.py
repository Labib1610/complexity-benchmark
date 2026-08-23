import sys

# Increase recursion depth just in case, though not needed for this iterative solution
sys.setrecursionlimit(2000)

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

    # Adjacency masks for bitwise operations
    # adj_mask[u] will store a bitmask where the v-th bit is 1 if u and v are connected
    adj_mask = [0] * (n + 1)
    # Adjacency lists for iteration (using sets to handle potential duplicates and allow sorting)
    adj = [set() for _ in range(n + 1)]
    
    for _ in range(m):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
        except StopIteration:
            break
        
        # Ensure u < v for consistency (undirected graph)
        if u > v:
            u, v = v, u
        
        # Update adjacency mask
        adj_mask[u] |= (1 << v)
        adj_mask[v] |= (1 << u)
        
        # Add to adjacency list
        adj[u].add(v)
        adj[v].add(u)
        
    # Convert sets to sorted lists to iterate neighbors in increasing order
    adj_list = [sorted(list(s)) for s in adj]
    
    # Iterate through each worker 'a'
    # Since we want the lexicographically smallest triple (a, b, c),
    # iterating 'a' from 1 to n ensures we find the smallest 'a' first.
    for a in range(1, n + 1):
        # Iterate through neighbors 'b' of 'a'
        # Since adj_list[a] is sorted, we encounter 'b' in increasing order.
        for b in adj_list[a]:
            # We require a < b < c.
            if b <= a:
                continue
            
            # We need to find a common neighbor 'c' such that c > b.
            # We want the smallest such 'c' to satisfy the lexicographical requirement.
            
            # Calculate common neighbors of a and b using bitwise AND
            common = adj_mask[a] & adj_mask[b]
            
            # We are interested in bits set in 'common' that are greater than 'b'.
            # Shifting 'common' right by (b + 1) moves the bit at position (b + 1 + k) to position k.
            # Bits at positions <= b are shifted out (become 0).
            shifted_common = common >> (b + 1)
            
            if shifted_common:
                # Find the lowest set bit in shifted_common.
                # (shifted_common & -shifted_common) isolates the lowest set bit.
                # bit_length() - 1 gives the 0-based index of that bit (which corresponds to the offset).
                offset = (shifted_common & -shifted_common).bit_length() - 1
                
                # Calculate actual position of c
                c = offset + b + 1
                
                # Found the lexicographically smallest triple
                print(f"{a} {b} {c}")
                return

if __name__ == '__main__':
    solve()
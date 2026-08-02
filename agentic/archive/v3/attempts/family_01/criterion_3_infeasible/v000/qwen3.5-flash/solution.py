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

    # Adjacency list to iterate over neighbors
    adj_list = [[] for _ in range(n + 1)]
    
    # Read edges
    # We store duplicates initially to simplify reading, then filter later
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj_list[u].append(v)
        adj_list[v].append(u)
        
    adj_mask = [0] * (n + 1)
    
    # Post-process adj_list: sort and unique, and build adjacency masks
    # Using sets to remove duplicates and then sorting ensures we process neighbors in increasing order
    for i in range(1, n + 1):
        if not adj_list[i]:
            continue
        # Use set to remove duplicates and sort
        adj_list[i] = sorted(list(set(adj_list[i])))
        
        # Build adjacency mask (integer bitmask)
        mask = 0
        for v in adj_list[i]:
            mask |= (1 << v)
        adj_mask[i] = mask
        
    # Iterate to find the lexicographically smallest triple (a, b, c) with a < b < c
    # We iterate 'a' from 1 to n to minimize 'a' first
    for a in range(1, n + 1):
        # Iterate 'b' in neighbors of 'a'. Since adj_list[a] is sorted, 'b' is increasing
        for b in adj_list[a]:
            if b <= a:
                continue
            
            # Check for common neighbor c > b
            # Common neighbors are represented by the bitwise AND of adjacency masks
            common = adj_mask[a] & adj_mask[b]
            
            # We need the smallest bit set in 'common' that is at a position > b
            # Shifting right by (b + 1) removes bits <= b
            shifted = common >> (b + 1)
            
            if shifted:
                # Find the lowest set bit in 'shifted'
                # (shifted & -shifted) isolates the lowest set bit
                low_bit = shifted & -shifted
                
                # The index of this bit in 'shifted' is (bit_length - 1)
                # The actual vertex index c is this index + (b + 1)
                c_rel = low_bit.bit_length() - 1
                c = c_rel + b + 1
                
                # Since we iterate 'a' and 'b' in increasing order, and pick the smallest 'c',
                # this is the lexicographically smallest triple.
                print(f"{a} {b} {c}")
                return

if __name__ == '__main__':
    main()
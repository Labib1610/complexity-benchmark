import sys

# Increase recursion depth just in case, though not needed for this iterative solution
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

    # Adjacency mask: adj_mask[u] is an integer where the v-th bit is 1 if u and v are connected.
    # We use 1-based indexing for vertices, so bit v corresponds to vertex v.
    # adj_mask will be a list of integers.
    adj_mask = [0] * (n + 1)
    
    # Adjacency list: adj_list[u] contains neighbors of u
    adj_list = [[] for _ in range(n + 1)]
    
    # Read m edges
    for _ in range(m):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
        except StopIteration:
            break
            
        # Update adjacency masks
        # Set bit v in adj_mask[u] and bit u in adj_mask[v]
        adj_mask[u] |= (1 << v)
        adj_mask[v] |= (1 << u)
        
        # Update adjacency lists
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    # Sort adjacency lists to ensure we iterate b in increasing order.
    # This is crucial for finding the lexicographically smallest triple.
    for i in range(1, n + 1):
        adj_list[i].sort()
        
    # Iterate a from 1 to n.
    # We want the smallest 'a' first.
    for a in range(1, n + 1):
        # Iterate neighbors b of a such that b > a.
        # Since adj_list[a] is sorted, we can iterate and skip b <= a.
        # We want the smallest 'b' next.
        for b in adj_list[a]:
            if b <= a:
                continue
            
            # We have edge (a, b) since b is in adj_list[a].
            # We need to find a common neighbor c of a and b such that c > b.
            # To minimize the triple (a, b, c) lexicographically, we need the smallest such c.
            
            # Find intersection of neighbors using bitwise AND
            common = adj_mask[a] & adj_mask[b]
            
            # We only care about bits c where c > b.
            # We create a mask that has 0s at positions 0 to b, and 1s elsewhere.
            # (1 << (b + 1)) - 1 creates a mask with 1s at 0 to b.
            # We invert it to get 0s at 0 to b.
            # Python's ~mask works correctly (infinite 1s to the left).
            
            mask = (1 << (b + 1)) - 1
            candidates = common & ~mask
            
            if candidates:
                # Find the lowest set bit in candidates.
                # (candidates & -candidates) isolates the lowest set bit.
                # bit_length() gives the number of bits required to represent the integer.
                # If the lowest set bit is at index k (value 2^k), bit_length is k+1.
                # So k = bit_length() - 1.
                # Since bit indices correspond to vertex numbers, this gives us 'c'.
                
                c = (candidates & -candidates).bit_length() - 1
                print(f"{a} {b} {c}")
                return

if __name__ == '__main__':
    main()
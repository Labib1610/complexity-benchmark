import sys

# Increase recursion depth just in case, though not strictly needed here
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

    # Adjacency masks using Python integers as bitsets
    # adj_mask[u] has bit (v-1) set if u and v are connected
    # Size n + 1 for 1-based indexing
    adj_mask = [0] * (n + 1)
    
    # Adjacency lists to iterate neighbors in sorted order
    adj_list = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        
        # Update masks: set bit corresponding to the neighbor
        # Vertex v corresponds to bit (v-1)
        adj_mask[u] |= (1 << (v - 1))
        adj_mask[v] |= (1 << (u - 1))
        
        # Update adjacency lists
        adj_list[u].append(v)
        adj_list[v].append(u)
        
    # Sort adjacency lists to ensure we process neighbors in increasing order.
    # This allows us to find the lexicographically smallest b for a given a.
    for i in range(1, n + 1):
        adj_list[i].sort()
        
    # Iterate to find the lexicographically smallest triple (a, b, c)
    # We want the smallest a, then smallest b, then smallest c.
    # Since we iterate a from 1 to n, we find the smallest a first.
    # For a fixed a, we iterate b in increasing order (from adj_list[a]).
    # For fixed a, b, we find the smallest c > b that forms a triangle.
    
    for a in range(1, n + 1):
        # Iterate neighbors of a
        for b in adj_list[a]:
            # We require a < b < c. So we only consider b > a.
            if b <= a:
                continue
            
            # We have edge (a, b). We need to find smallest c > b
            # such that (a, c) and (b, c) are edges.
            # Common neighbors of a and b are given by the bitwise AND of their masks.
            common = adj_mask[a] & adj_mask[b]
            
            # We are interested in neighbors c > b.
            # In terms of bit indices, vertex c corresponds to bit (c-1).
            # Condition c > b implies c-1 >= b.
            # So we look for set bits in 'common' at indices >= b.
            
            # Shift right by b to bring bit b to position 0.
            # This discards bits 0 to b-1 (vertices 1 to b).
            shifted = common >> b
            
            if shifted > 0:
                # There exists at least one common neighbor c > b.
                # We need the smallest such c.
                # This corresponds to the lowest set bit in 'shifted'.
                # (shifted & -shifted) isolates the lowest set bit.
                # bit_length() returns the number of bits required to represent an integer.
                # For 2^k, bit_length is k+1.
                # So the index k of the lowest set bit is bit_length - 1.
                k = (shifted & -shifted).bit_length() - 1
                
                # The vertex corresponding to bit index k in 'shifted'
                # corresponds to bit index b + k in 'common'.
                # Vertex index = bit_index + 1.
                c = b + 1 + k
                
                print(f"{a} {b} {c}")
                return

if __name__ == '__main__':
    solve()
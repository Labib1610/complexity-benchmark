import sys

# Increase recursion depth just in case, though not used here
sys.setrecursionlimit(2000)

def solve():
    # Read all input from standard input efficiently
    # Using sys.stdin.read().split() handles all whitespace (newlines, spaces) automatically
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
    
    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Adjacency bitmasks
    # adj[u] will have bit v set if u and v are connected
    # We use 1-based indexing for nodes, so bit i corresponds to node i
    # Using integers as bitmasks allows for fast intersection operations
    adj = [0] * (n + 1)
    
    # Adjacency lists to iterate neighbors in sorted order
    # This is needed to find the lexicographically smallest triple efficiently
    adj_list = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        
        # Set bits
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
        
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    # Sort adjacency lists to ensure we iterate b in increasing order
    # Sorting takes O(m log m) or O(m log n), which is efficient enough
    for i in range(1, n + 1):
        adj_list[i].sort()
        
    # Iterate a from 1 to n
    # We need to output the lexicographically smallest triple (a, b, c) with a < b < c
    # Since we iterate a from 1 upwards, the first valid triple found will have the smallest a.
    # Inside the loop for a, we iterate b in increasing order, ensuring smallest b.
    # Then we find smallest c.
    for a in range(1, n + 1):
        mask_a = adj[a]
        
        # Iterate neighbors b of a such that b > a
        # Since adj_list[a] is sorted, we iterate and check the condition
        for b in adj_list[a]:
            if b <= a:
                continue
            
            # We need to find c > b such that (a, c) and (b, c) are edges.
            # common = neighbors of a AND neighbors of b
            # Bitwise AND is efficient (O(n/64))
            common = mask_a & adj[b]
            
            # We need c > b.
            # Shift common right by (b + 1) to remove bits <= b.
            # This effectively filters for neighbors with index > b.
            shifted = common >> (b + 1)
            
            if shifted:
                # shifted has bits set for valid c's.
                # We want the smallest c, which corresponds to the lowest set bit (LSB).
                # The LSB value is (shifted & -shifted).
                # bit_length() returns the number of bits required to represent the integer.
                # For 2^k, bit_length is k + 1.
                # So the index k (0-based) is bit_length - 1.
                # The position in 'shifted' is k.
                # The original position in 'common' is k + b + 1.
                # Since we mapped node i to bit i, the node number c is k + b + 1.
                
                c = b + 1 + (shifted & -shifted).bit_length() - 1
                print(f"{a} {b} {c}")
                return

if __name__ == '__main__':
    solve()
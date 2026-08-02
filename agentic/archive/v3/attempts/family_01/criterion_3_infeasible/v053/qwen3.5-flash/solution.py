import sys

# Increase recursion depth just in case, though not needed here
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

    # Use a list of integers for bitmask representation of adjacency.
    # adj_mask[u] will have the k-th bit set if there is an edge between u and k.
    # Since nodes are 1-indexed, we use bits 1 to n.
    adj_mask = [0] * (n + 1)
    
    # Use adjacency lists to iterate over neighbors in sorted order
    # to ensure lexicographical order (minimize a, then b, then c).
    # We use sets initially to handle potential duplicate edges in input.
    adj_list = [set() for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        
        # Update bitmask
        adj_mask[u] |= (1 << v)
        adj_mask[v] |= (1 << u)
        
        # Update adjacency list
        adj_list[u].add(v)
        adj_list[v].add(u)
            
    # Sort adjacency lists to guarantee increasing order of neighbors
    for i in range(1, n + 1):
        adj_list[i] = sorted(list(adj_list[i]))
        
    # Iterate to find the lexicographically smallest triangle
    # We want to minimize a, then b, then c.
    # Iterate a from 1 to n.
    for a in range(1, n + 1):
        # Iterate b from neighbors of a. Since adj_list[a] is sorted,
        # we encounter b in increasing order.
        for b in adj_list[a]:
            if b <= a:
                continue  # We need b > a
            
            # We need to find c such that c > b and c is connected to both a and b.
            # The set of common neighbors is represented by bitwise AND.
            common = adj_mask[a] & adj_mask[b]
            
            # We need c > b. So we must clear bits corresponding to nodes <= b.
            # Node k corresponds to bit k.
            # We want to clear bits 1 to b.
            # The mask (1 << (b + 1)) - 1 has bits 0 to b set.
            # ~mask has bits 0 to b unset (and higher bits set).
            # Note: Python integers are arbitrary precision, so bitwise operations work as expected.
            clear_mask = (1 << (b + 1)) - 1
            common &= ~clear_mask
            
            if common == 0:
                continue
            
            # Find the smallest c. This corresponds to the lowest set bit in 'common'.
            # common & -common isolates the lowest set bit (LSB).
            lsb = common & -common
            
            # If bit k is set (value 2^k), bit_length is k + 1.
            # We want node index k.
            c = lsb.bit_length() - 1
            
            # Since we iterate a increasing, then b increasing, then find smallest c,
            # the first valid triple found is the lexicographically smallest.
            print(f"{a} {b} {c}")
            return

if __name__ == '__main__':
    solve()
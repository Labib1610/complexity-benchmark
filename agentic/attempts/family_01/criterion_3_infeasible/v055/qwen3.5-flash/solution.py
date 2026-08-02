import sys

# Increase recursion depth just in case, though not used here.
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

    # Precompute powers of 2 for fast bitmask updates.
    # powers_of_2[i] corresponds to 1 << i, representing node i (1-based index).
    # This avoids creating large integer objects repeatedly.
    powers_of_2 = [1 << i for i in range(n + 1)]
    
    # adj[i] will store an integer where the k-th bit is set if node k is connected to i.
    adj = [0] * (n + 1)
    
    # adj_list[i] stores the list of neighbors of i.
    adj_list = [[] for _ in range(n + 1)]
    
    # Read edges
    for _ in range(m):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
        except StopIteration:
            break
        
        # Update adjacency bitmasks
        adj[u] |= powers_of_2[v]
        adj[v] |= powers_of_2[u]
        
        # Update adjacency lists
        adj_list[u].append(v)
        adj_list[v].append(u)
        
    # Sort adjacency lists to ensure we iterate neighbors in increasing order.
    # This is crucial for finding the lexicographically smallest triplet (a, b, c).
    for i in range(1, n + 1):
        adj_list[i].sort()
        
    # Iterate through each station a from 1 to n.
    # We want to find the smallest a, then smallest b > a, then smallest c > b.
    for a in range(1, n + 1):
        # Iterate through neighbors b of a.
        for b in adj_list[a]:
            # We only consider b > a to satisfy a < b < c condition.
            # Since adj_list[a] is sorted, we can skip smaller neighbors.
            if b <= a:
                continue
            
            # Find common neighbors of a and b.
            # Using bitwise AND on the integer bitmasks is very efficient.
            common = adj[a] & adj[b]
            
            # If no common neighbors, continue to next b.
            if common == 0:
                continue
            
            # We need the smallest common neighbor c such that c > b.
            # This corresponds to the lowest set bit in 'common' at a position > b.
            # To ignore bits <= b, we can right-shift 'common' by (b + 1).
            # The position of the lowest set bit in the shifted value will give us the offset.
            shifted = common >> (b + 1)
            
            if shifted > 0:
                # Get the lowest set bit of 'shifted'.
                # In two's complement, -shifted has only the lowest set bit of shifted set.
                lowest = shifted & -shifted
                
                # bit_length() returns the number of bits required to represent an integer.
                # For a power of 2 (2^k), bit_length is k + 1.
                # The index of the bit (0-based) is k.
                k = lowest.bit_length() - 1
                
                # The actual node index c is k + (b + 1).
                c = k + b + 1
                
                # Since we iterate a, then b, then find the smallest c, the first valid triplet found
                # is guaranteed to be the lexicographically smallest.
                print(f"{a} {b} {c}")
                return

if __name__ == '__main__':
    solve()
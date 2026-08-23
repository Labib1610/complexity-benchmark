import sys

# Increase recursion depth just in case
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
    
    adj = [[] for _ in range(n + 1)]
    masks = [0] * (n + 1)
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        
        adj[u].append(v)
        adj[v].append(u)
        
        # Set bits. Nodes are 1..n, bits 0..n-1.
        masks[u] |= (1 << (v - 1))
        masks[v] |= (1 << (u - 1))
    
    # Sort adjacency lists to ensure we iterate in increasing order
    # This is crucial for finding the lexicographically smallest triple
    for i in range(1, n + 1):
        adj[i].sort()
        
    # Iterate a from 1 to n to find the smallest 'a'
    for a in range(1, n + 1):
        # Iterate neighbors u of a. u corresponds to 'b' in the triple (a, b, c).
        # We need b > a.
        for u in adj[a]:
            if u <= a:
                continue
            
            # We need to find smallest v > u such that v is connected to a and u.
            # Intersection of neighbors of a and u: masks[a] & masks[u]
            # We need bit v-1 set in intersection.
            # And v > u => v-1 >= u.
            # So we look for bits in intersection with index >= u.
            
            common = masks[a] & masks[u]
            
            # Shift right by u to check bits starting from u.
            # If bit u is set (corresponding to node u+1), it becomes bit 0.
            # If bit v-1 is set, it moves to position (v-1) - u.
            shifted = common >> u
            
            if shifted:
                # Find the lowest set bit in shifted.
                # This corresponds to the smallest v > u.
                lsb = shifted & -shifted
                # lsb is 2^k, where k is the index in the shifted value.
                # The original bit index was k + u.
                # The node index v is original bit index + 1.
                # k = lsb.bit_length() - 1
                v = (lsb.bit_length() - 1) + u + 1
                
                # Since we iterate a in increasing order, and u (neighbors of a) in increasing order,
                # and we pick the smallest v, the first triple we find is the lexicographically smallest.
                print(f"{a} {u} {v}")
                return

if __name__ == '__main__':
    solve()
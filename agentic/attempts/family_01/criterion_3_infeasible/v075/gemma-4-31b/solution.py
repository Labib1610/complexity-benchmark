import sys

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Adjacency list for graph
    adj = [[] for _ in range(n + 1)]
    # Adjacency matrix using bitsets (represented by integers in Python)
    # Since n <= 2000, we can use integers as bitsets to check existence of edges quickly.
    bit_adj = [0] * (n + 1)
    
    ptr = 2
    for _ in range(m):
        u = int(input_data[ptr])
        v = int(input_data[ptr + 1])
        ptr += 2
        adj[u].append(v)
        adj[v].append(u)
        bit_adj[u] |= (1 << v)
        bit_adj[v] |= (1 << u)
        
    # Sort adjacency lists to ensure we check in lexicographical order
    for i in range(1, n + 1):
        adj[i].sort()
        
    # We want to find the lexicographically smallest (a, b, c) where a < b < c
    # Iterate through all possible 'a' from 1 to n
    for a in range(1, n + 1):
        # Candidates for 'b' must be neighbors of 'a' and b > a
        neighbors_a = [v for v in adj[a] if v > a]
        
        # To find the smallest 'b' and then 'c', we iterate through neighbors of 'a'
        # in increasing order.
        for b in neighbors_a:
            # Now we need 'c' such that c > b and c is a neighbor of both a and b.
            # We can find the intersection of neighbors of a and neighbors of b.
            # Using bitwise AND on the bitsets is very efficient.
            common = bit_adj[a] & bit_adj[b]
            
            # We need the smallest c > b.
            # We can find the lowest set bit in 'common' that is greater than b.
            # Mask out bits <= b
            mask = ~((1 << (b + 1)) - 1)
            possible_c = common & mask
            
            if possible_c:
                # Find the index of the lowest set bit
                # (possible_c & -possible_c).bit_length() - 1 gives the index
                c = (possible_c & -possible_c).bit_length() - 1
                print(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()
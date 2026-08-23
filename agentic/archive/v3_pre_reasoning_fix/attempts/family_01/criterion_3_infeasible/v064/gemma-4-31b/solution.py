import sys

def solve():
    # Increase recursion depth if necessary, though not needed for this approach
    sys.setrecursionlimit(2000)
    
    # Read n and m
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Use an adjacency list to store the graph
    adj = [[] for _ in range(n + 1)]
    # Use a bitset-like approach (using Python's large integers) for fast intersection
    # or a set for each node. Given n=2000, bitsets (integers) are very efficient.
    bit_adj = [0] * (n + 1)
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
        bit_adj[u] |= (1 << v)
        bit_adj[v] |= (1 << u)
    
    # Sort adjacency lists to ensure we process nodes in increasing order
    for i in range(1, n + 1):
        adj[i].sort()
    
    # We need the lexicographically smallest (a, b, c) with a < b < c.
    # Iterate through all possible 'a' from 1 to n.
    for a in range(1, n + 1):
        # To find b and c such that a < b < c and (a,b), (a,c), (b,c) are edges:
        # b must be a neighbor of a and b > a.
        # c must be a neighbor of a and c > b.
        # (b, c) must be an edge.
        
        # Filter neighbors of a that are greater than a
        candidates = [v for v in adj[a] if v > a]
        
        # Iterate through these candidates as potential 'b'
        for i in range(len(candidates)):
            b = candidates[i]
            
            # Now we need c such that c > b and c is a neighbor of both a and b.
            # The candidates list contains all neighbors of a that are > a.
            # We only care about those that are also > b.
            # The intersection of neighbors of a and neighbors of b gives us the common nodes.
            
            # bit_adj[a] & bit_adj[b] gives nodes connected to both.
            common = bit_adj[a] & bit_adj[b]
            
            # We need the smallest c > b.
            # Since we want lexicographically smallest, we should check
            # candidates from the list that are > b.
            for j in range(i + 1, len(candidates)):
                c = candidates[j]
                if (common >> c) & 1:
                    print(f"{a} {b} {c}")
                    return

if __name__ == "__main__":
    solve()
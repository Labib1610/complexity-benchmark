import sys

def solve():
    # Increase recursion depth just in case, although not needed for this approach
    sys.setrecursionlimit(2000)
    
    # Read n and m
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Use adjacency sets for O(1) lookup of edges
    adj = [set() for _ in range(n + 1)]
    # To iterate in lexicographical order, we'll use sorted adjacency lists
    adj_list = [[] for _ in range(n + 1)]
    
    ptr = 2
    for _ in range(m):
        u = int(input_data[ptr])
        v = int(input_data[ptr + 1])
        ptr += 2
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
        adj_list[u].append(v)
        adj_list[v].append(u)
        
    # Sort adjacency lists to facilitate lexicographical search
    for i in range(1, n + 1):
        adj_list[i].sort()

    # We need the lexicographically smallest (a, b, c) where a < b < c.
    # We iterate through possible 'a' values from 1 to n.
    for a in range(1, n + 1):
        # For a fixed 'a', we look for b and c such that a < b < c and (a,b), (a,c), (b,c) are edges.
        # Only consider neighbors of 'a' that are greater than 'a'.
        neighbors_of_a = [v for v in adj_list[a] if v > a]
        
        # To find the lexicographically smallest (b, c), we iterate through
        # neighbors_of_a in increasing order.
        for i in range(len(neighbors_of_a)):
            b = neighbors_of_a[i]
            # Now we need c such that c > b and c is a neighbor of both a and b.
            # Since neighbors_of_a is sorted, we only check neighbors_of_a[j] where j > i.
            for j in range(i + 1, len(neighbors_of_a)):
                c = neighbors_of_a[j]
                # Check if (b, c) is an edge.
                if c in adj[b]:
                    print(f"{a} {b} {c}")
                    return

if __name__ == "__main__":
    solve()
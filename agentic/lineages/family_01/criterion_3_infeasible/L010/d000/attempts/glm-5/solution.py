import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [set() for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].add(v)
        adj[v].add(u)
    
    # To find the lexicographically smallest triple (a, b, c),
    # we iterate a from 1 to n, then b from a+1 to n, then c from b+1 to n.
    # We need to check if (a,b), (a,c), (b,c) are all edges.
    # Checking (a,b) and (a,c) is O(1) using adjacency sets.
    # Checking (b,c) is O(1) using adjacency sets.
    # Total complexity O(n^3) is too slow for n=2000.
    # We optimize by iterating a, then b > a such that (a,b) is an edge.
    # Then we iterate c > b such that (a,c) is an edge.
    # Finally we check if (b,c) is an edge.
    # Since m <= 2*10^5, the number of pairs (a,b) and (a,c) is limited.
    # The complexity is roughly proportional to sum over a of (deg(a))^2.
    # With m=2e5, sum of squares is maximized when one node has ~2e5 edges,
    # leading to ~4e10 operations in worst case, which is too slow.
    # However, we can iterate c in increasing order and stop at the first valid triple.
    # To speed up the check for (b,c), we can use a boolean matrix for small degrees.
    
    # Threshold for using matrix vs set lookup
    # If degree is small, iterating neighbors is fast.
    # If degree is large, matrix lookup is O(1).
    # We use a threshold of approx sqrt(M) ~ 450.
    threshold = 450
    
    # Identify heavy nodes
    is_heavy = [False] * (n + 1)
    for i in range(1, n + 1):
        if len(adj[i]) >= threshold:
            is_heavy[i] = True
    
    # Create adjacency matrix for heavy nodes
    # heavy_indices maps node number to index in heavy_nodes list
    heavy_nodes = [i for i in range(1, n + 1) if is_heavy[i]]
    heavy_indices = {node: i for i, node in enumerate(heavy_nodes)}
    num_heavy = len(heavy_nodes)
    
    # adj_matrix[k] is a list of booleans for heavy nodes
    # adj_matrix[k][l] is True if heavy_nodes[k] and heavy_nodes[l] are connected
    adj_matrix = []
    for u in heavy_nodes:
        row = [False] * num_heavy
        for v in adj[u]:
            if is_heavy[v]:
                row[heavy_indices[v]] = True
        adj_matrix.append(row)
    
    # Iterate to find the lexicographically smallest triple
    for a in range(1, n + 1):
        # We need b > a and c > b
        # Filter neighbors of a that are > a
        neighbors_a = [v for v in adj[a] if v > a]
        # Sort to ensure we check in increasing order
        neighbors_a.sort()
        
        # Iterate over b
        for i in range(len(neighbors_a)):
            b = neighbors_a[i]
            # Iterate over c
            for j in range(i + 1, len(neighbors_a)):
                c = neighbors_a[j]
                # Check if b and c are connected
                connected = False
                if is_heavy[b] and is_heavy[c]:
                    connected = adj_matrix[heavy_indices[b]][heavy_indices[c]]
                elif is_heavy[b]:
                    # c is light, check if b is in adj[c]
                    # Since c is light, adj[c] is small, but we are checking adj[b] which is large
                    # Actually, if b is heavy, we should check if c is in adj[b]?
                    # adj[b] is a set, so c in adj[b] is O(1) average.
                    # But we constructed adj_matrix for heavy-heavy.
                    # For heavy-light, we can just use the set.
                    connected = (c in adj[b])
                elif is_heavy[c]:
                    connected = (b in adj[c])
                else:
                    # Both light, use set intersection or just check membership
                    # Since both are light, checking c in adj[b] is fast
                    connected = (c in adj[b])
                
                if connected:
                    print(f"{a} {b} {c}")
                    return

if __name__ == '__main__':
    solve()
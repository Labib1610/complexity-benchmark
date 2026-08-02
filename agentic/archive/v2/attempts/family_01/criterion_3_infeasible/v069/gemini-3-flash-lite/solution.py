import sys

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Use adjacency sets for O(1) edge lookups
    adj = [set() for _ in range(n + 1)]
    edges = []
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        adj[u].add(v)
        adj[v].add(u)
        edges.append((min(u, v), max(u, v)))
        idx += 2
    
    # Sort edges to ensure we check triples in lexicographical order
    # A triple (a, b, c) with a < b < c is found if we have an edge (a, b)
    # and we check all nodes c > b such that c is connected to both a and b.
    edges.sort()
    
    # To get the lexicographically smallest (a, b, c), we iterate
    # through all possible a, then all possible b > a, then all possible c > b.
    # Since n <= 2000, O(n^3) is too slow, but O(m * n) or O(n * edges_per_node) is fine.
    
    for a in range(1, n + 1):
        # Get neighbors of a that are greater than a
        neighbors_a = [v for v in adj[a] if v > a]
        neighbors_a.sort()
        
        for i in range(len(neighbors_a)):
            b = neighbors_a[i]
            # Now we look for a c > b such that c is in both adj[a] and adj[b]
            # To be lexicographically smallest, we check candidates in increasing order
            # The intersection of adj[a] and adj[b] provides all c
            common = adj[a].intersection(adj[b])
            for c in sorted(list(common)):
                if c > b:
                    print(f"{a} {b} {c}")
                    return

if __name__ == '__main__':
    solve()
import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    adj = [set() for _ in range(n + 1)]
    
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # For each node, sort its neighbors for consistent processing
    for i in range(1, n + 1):
        adj[i] = sorted(adj[i])
    
    # We'll iterate through all edges (u,v) and look for a common neighbor w
    # such that u-v, v-w, and u-w all exist (forming a triangle)
    # We want the lexicographically smallest such triangle
    
    best = None
    
    # To find the lex smallest triangle efficiently:
    # Iterate through each vertex u from 1 to n
    # For each u, consider its neighbors v > u
    # For each such v, look for a neighbor w of both u and v such that w > v
    # This ensures u < v < w and we process in lex order
    
    for u in range(1, n + 1):
        neighbors_u = adj[u]
        # Only consider neighbors greater than u to maintain order
        candidates_v = [v for v in neighbors_u if v > u]
        # Now for each pair (u,v), find a common neighbor w > v
        for i in range(len(candidates_v)):
            v = candidates_v[i]
            # Get neighbors of v that are > v
            neighbors_v = adj[v]
            candidates_w = [w for w in neighbors_v if w > v]
            # Convert u's neighbors > v to a set for fast lookup
            neighbors_u_set = set([w for w in neighbors_u if w > v])
            # Check for intersection
            for w in candidates_w:
                if w in neighbors_u_set:
                    # Found triangle u-v-w with u < v < w
                    return print(u, v, w)
    
    # As per problem statement, a triangle is guaranteed to exist
    # So we should always return before reaching here

if __name__ == "__main__":
    main()
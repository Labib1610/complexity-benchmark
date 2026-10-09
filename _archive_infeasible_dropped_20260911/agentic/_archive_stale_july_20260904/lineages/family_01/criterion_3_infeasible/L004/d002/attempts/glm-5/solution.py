import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [set() for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
    
    # Sort edges lexicographically
    edges.sort()
    
    # For each edge (u, v), check if there exists w such that
    # w is connected to both u and v, and u < v < w
    # This ensures we find the lexicographically smallest triangle
    
    # Build adjacency lists sorted for iteration
    adj_list = [sorted(s) for s in adj]
    
    for u, v in edges:
        # Find common neighbors w where w > v
        # Since we process edges in sorted order, first such w gives smallest triangle
        i, j = 0, 0
        list_u = adj_list[u]
        list_v = adj_list[v]
        len_u, len_v = len(list_u), len(list_v)
        
        while i < len_u and j < len_v:
            w_u = list_u[i]
            w_v = list_v[j]
            if w_u == w_v:
                w = w_u
                if w > v:
                    print(u, v, w)
                    return
                i += 1
                j += 1
            elif w_u < w_v:
                i += 1
            else:
                j += 1
    
    # Fallback: check all edges without the w > v constraint
    # This handles cases where the triangle might not satisfy w > v
    for u, v in edges:
        for w in adj[u]:
            if w != v and w in adj[v]:
                result = sorted([u, v, w])
                print(result[0], result[1], result[2])
                return

if __name__ == "__main__":
    solve()
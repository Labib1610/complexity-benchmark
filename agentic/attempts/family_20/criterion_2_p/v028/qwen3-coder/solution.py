import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n_V, n_D, m = map(int, sys.stdin.readline().split())
    
    # We'll build a bipartite graph: V on one side, D on the other
    # Edges represent transfers
    
    # For each vertex (both V and D), store list of adjacent edges (by index)
    adj = defaultdict(list)
    edges = []
    
    for i in range(m):
        u, v = map(int, sys.stdin.readline().split())
        # Convert to 0-based indexing
        u -= 1
        v -= 1
        # We'll encode dock nodes as v + n_V to distinguish from vessels
        edges.append((u, v + n_V))
        adj[u].append(i)
        adj[v + n_V].append(i)
    
    # Find maximum degree
    max_degree = 0
    for key in adj:
        max_degree = max(max_degree, len(adj[key]))
    
    if max_degree == 0:
        print("YES")
        print()
        return
    
    # We need to edge-color the bipartite graph with max_degree colors
    # This is always possible for bipartite graphs (König's theorem)
    
    # We use a greedy algorithm with BFS-like approach
    
    # Result array to store day for each transfer (0-based, we'll add 1 at the end)
    result = [-1] * m
    
    # For each node, keep track of which "colors" (days) it's already used
    used = [set() for _ in range(n_V + n_D)]
    
    # Process edges in some order - we can just go through them
    # But to make it work well, we can process nodes in order of decreasing degree
    # Or just process edges in order and assign first available color
    
    # A simple greedy method:
    # For each edge, pick the lowest-numbered day not used by either endpoint
    
    for i in range(m):
        u, v_node = edges[i]
        # v_node is v + n_V
        day = 1
        while day in used[u] or day in used[v_node]:
            day += 1
        result[i] = day
        used[u].add(day)
        used[v_node].add(day)
    
    print("YES")
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
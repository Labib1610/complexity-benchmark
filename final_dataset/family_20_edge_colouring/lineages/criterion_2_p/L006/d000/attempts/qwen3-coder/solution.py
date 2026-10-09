import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    nL, nR, m = map(int, sys.stdin.readline().split())
    
    # Build adjacency lists for left and right ports
    left_adj = defaultdict(list)   # left port -> list of right ports
    right_adj = defaultdict(list)  # right port -> list of left ports
    
    edges = []
    
    for i in range(m):
        u, v = map(int, sys.stdin.readline().split())
        left_adj[u].append(v)
        right_adj[v].append(u)
        edges.append((u, v))
    
    # Compute degree of each port
    left_degree = {u: len(left_adj[u]) for u in left_adj}
    right_degree = {v: len(right_adj[v]) for v in right_adj}
    
    # Find maximum degree Δ
    Delta = 0
    for d in left_degree.values():
        if d > Delta:
            Delta = d
    for d in right_degree.values():
        if d > Delta:
            Delta = d
    
    # If no cables, output YES and empty line
    if m == 0:
        print("YES")
        return
    
    # We need to edge-color the bipartite graph with Delta colors
    # This is always possible by Kőnig's theorem since max degree is Delta
    
    # We'll use a greedy approach with BFS-like processing
    # For each node, we'll keep track of which colors are used on its edges
    
    # To make it efficient, process nodes in order, assigning colors greedily
    
    # Let's try a different approach: since it's bipartite, we can use the fact that
    # we can always color it with Δ colors.
    
    # We'll build the coloring incrementally.
    # For each edge, assign it the lowest numbered color not used by its endpoints
    
    # For efficiency, for each vertex, maintain a set of used colors
    left_used = defaultdict(set)   # left port -> set of used colors
    right_used = defaultdict(set)  # right port -> set of used colors
    
    result = []
    
    for u, v in edges:
        # Find the first color from 1 to Delta not in left_used[u] or right_used[v]
        used_colors = left_used[u] | right_used[v]
        color = 1
        while color in used_colors:
            color += 1
        result.append(color)
        left_used[u].add(color)
        right_used[v].add(color)
    
    print("YES")
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
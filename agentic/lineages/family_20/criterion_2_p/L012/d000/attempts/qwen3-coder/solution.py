import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    nA, nB, m = map(int, sys.stdin.readline().split())
    
    # Build adjacency lists for both sides
    adjA = defaultdict(list)  # adjA[u] = list of (v, idx)
    adjB = defaultdict(list)  # adjB[v] = list of (u, idx)
    
    edges = []
    for i in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adjA[u].append((v, i))
        adjB[v].append((u, i))
        edges.append((u, v))
    
    # Determine the maximum degree
    max_degree = 0
    for u in range(1, nA + 1):
        max_degree = max(max_degree, len(adjA[u]))
    for v in range(1, nB + 1):
        max_degree = max(max_degree, len(adjB[v]))
    
    if max_degree == 0:
        print("YES")
        return
    
    # Color the edges: each color represents a service window
    # We'll use a greedy edge coloring approach based on the maximum degree
    result = [0] * m  # result[i] = color (window) for edge i
    
    # For each node in A, we need to assign distinct colors to its edges
    # Similarly for each node in B
    
    # For each node, keep track of which colors are used by its neighbors
    # But a better way is to process edges and assign the smallest available color
    
    # Let's do a greedy coloring:
    # For each edge, assign the smallest color not used by either endpoint
    
    # For each vertex, maintain a set of used colors
    used_colors_A = [set() for _ in range(nA + 1)]
    used_colors_B = [set() for _ in range(nB + 1)]
    
    # To efficiently find the first available color, we can just iterate
    for i in range(m):
        u, v = edges[i]
        # Find the first color >= 1 not in used_colors_A[u] or used_colors_B[v]
        color = 1
        while color in used_colors_A[u] or color in used_colors_B[v]:
            color += 1
        result[i] = color
        used_colors_A[u].add(color)
        used_colors_B[v].add(color)
    
    print("YES")
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
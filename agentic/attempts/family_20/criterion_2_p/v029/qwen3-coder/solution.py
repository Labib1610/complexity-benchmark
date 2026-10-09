import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    nA = int(data[idx])
    idx += 1
    nB = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    
    edges = []
    adj = defaultdict(list)
    
    for i in range(m):
        u = int(data[idx]) - 1  # Convert to 0-based
        idx += 1
        v = int(data[idx]) - 1  # Convert to 0-based
        idx += 1
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v + nA].append((u, i))
    
    # Find maximum degree
    max_degree = 0
    for u in range(nA + nB):
        max_degree = max(max_degree, len(adj[u]))
    
    if max_degree == 0:
        print("YES")
        print()
        return
    
    # Color the edges: each edge gets a color 0 to max_degree - 1
    # This is edge coloring on a bipartite graph, which can be done with max_degree colors
    
    # We'll use a greedy approach with BFS for each node to assign colors
    result = [-1] * m
    used_colors = [set() for _ in range(nA + nB)]  # For each node, which colors are used on its edges
    
    for i in range(m):
        u, v = edges[i]
        v_shifted = v + nA
        # Find a color not used by u or v
        color = 0
        while color in used_colors[u] or color in used_colors[v_shifted]:
            color += 1
        result[i] = color
        used_colors[u].add(color)
        used_colors[v_shifted].add(color)
    
    print("YES")
    print(' '.join(str(c + 1) for c in result))

if __name__ == "__main__":
    main()
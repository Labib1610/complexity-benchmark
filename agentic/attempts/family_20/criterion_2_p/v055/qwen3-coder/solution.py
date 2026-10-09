import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n_L = int(data[0])
    n_R = int(data[1])
    m = int(data[2])
    
    edges = []
    left_deg = [0] * (n_L + 1)
    right_deg = [0] * (n_R + 1)
    
    idx = 3
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        idx += 2
        edges.append((u, v))
        left_deg[u] += 1
        right_deg[v] += 1
    
    K = max(max(left_deg), max(right_deg))
    
    # Build adjacency list for the bipartite graph
    adj = [[] for _ in range(n_L + n_R + 2)]
    source = 0
    sink = n_L + n_R + 1
    
    # Add edges from source to left nodes
    for i in range(1, n_L + 1):
        adj[source].append((i, left_deg[i]))
    
    # Add edges from right nodes to sink
    for i in range(1, n_R + 1):
        adj[n_L + i].append((sink, right_deg[i]))
    
    # Add edges from left to right based on transfers
    edge_index = defaultdict(list)
    for i, (u, v) in enumerate(edges):
        adj[u].append((n_L + v, 1))
        edge_index[(u, n_L + v)].append(i)
    
    # Now we need to find a valid flow that assigns colors
    # We'll simulate a flow network and assign colors incrementally
    
    # For each left node, maintain which colors are used
    left_colors_used = [set() for _ in range(n_L + 1)]
    right_colors_used = [set() for _ in range(n_R + 1)]
    
    result = [0] * m
    
    for i, (u, v) in enumerate(edges):
        # Find a color not used by u or v
        color = 1
        while color in left_colors_used[u] or color in right_colors_used[v]:
            color += 1
        result[i] = color
        left_colors_used[u].add(color)
        right_colors_used[v].add(color)
    
    print("YES")
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
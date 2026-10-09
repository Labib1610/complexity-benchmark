import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n_in = int(data[0])
    n_out = int(data[1])
    m = int(data[2])
    
    links = []
    ingress_deg = [0] * (n_in + 1)
    egress_deg = [0] * (n_out + 1)
    ingress_adj = defaultdict(list)
    egress_adj = defaultdict(list)
    
    idx = 3
    for i in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        idx += 2
        links.append((u, v))
        ingress_deg[u] += 1
        egress_deg[v] += 1
        ingress_adj[u].append(i)
        egress_adj[v].append(i)
    
    delta = max(max(ingress_deg), max(egress_deg))
    
    # Color the edges: each link gets a color from 1 to delta
    # such that no two links incident to the same vertex have the same color
    
    # This is edge coloring, and since the graph is bipartite (ingress and egress),
    # we can use the fact that the chromatic index equals the maximum degree.
    
    # We'll use a greedy approach with available colors per vertex
    
    result = [0] * m
    ingress_colors = [set() for _ in range(n_in + 1)]
    egress_colors = [set() for _ in range(n_out + 1)]
    
    # Process links one by one
    for i in range(m):
        u, v = links[i]
        # Find a color not used by u or v
        used = ingress_colors[u] | egress_colors[v]
        color = 1
        while color in used:
            color += 1
        result[i] = color
        ingress_colors[u].add(color)
        egress_colors[v].add(color)
    
    print("YES")
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    nL = int(data[idx])
    idx += 1
    nR = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    
    edges = []
    deg = [0] * (nL + nR + 1)  # 1-based indexing for both L and R
    
    for _ in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        edges.append((u, v))
        deg[u] += 1
        deg[nL + v] += 1
    
    delta = max(deg) if deg else 0
    
    # Create adjacency list for the bipartite graph
    adj = defaultdict(list)
    for i, (u, v) in enumerate(edges):
        adj[u].append((v, i))
        adj[nL + v].append((u, i))
    
    # Color assignment for each edge
    result = [0] * m
    color = [0] * (nL + nR + 1)
    
    # For each node, we'll maintain which colors are used by its edges
    used_colors = [set() for _ in range(nL + nR + 1)]
    
    # Process each edge
    for i, (u, v) in enumerate(edges):
        c = 1
        # Find the first color not used by either u or v
        while c in used_colors[u] or c in used_colors[nL + v]:
            c += 1
        result[i] = c
        used_colors[u].add(c)
        used_colors[nL + v].add(c)
    
    print("YES")
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
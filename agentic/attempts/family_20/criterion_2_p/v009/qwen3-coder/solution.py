import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    nL = int(data[0])
    nR = int(data[1])
    m = int(data[2])
    
    edges = []
    adj = defaultdict(list)
    
    idx = 3
    for i in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx+1]) - 1
        idx += 2
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v + nL].append((u, i))
    
    # Compute the maximum degree
    max_degree = 0
    degree = [0] * (nL + nR)
    for i in range(nL):
        degree[i] = len(adj[i])
        max_degree = max(max_degree, degree[i])
    for i in range(nR):
        degree[i + nL] = len(adj[i + nL])
        max_degree = max(max_degree, degree[i + nL])
    
    if m == 0:
        print("YES")
        return
    
    # Color the edges: each edge gets a color from 1 to max_degree
    # This is edge coloring in a bipartite graph, which can be done with max_degree colors
    
    result = [0] * m
    used = [set() for _ in range(nL + nR)]
    
    # For each node on the left, we maintain a queue of its edges
    # We process edges in a way that ensures we can always color them properly
    
    # A simple greedy approach works because the graph is bipartite
    # and we have exactly Δ colors available
    
    # For each left node, assign colors to its edges avoiding conflicts at both ends
    for u in range(nL):
        if not adj[u]:
            continue
        # Available colors for this node u
        available = set(range(1, max_degree + 1))
        # Temporarily remove colors used by current edges of u
        for v, e_id in adj[u]:
            if result[e_id] != 0:
                available.discard(result[e_id])
        
        # Assign colors to unassigned edges
        for v, e_id in adj[u]:
            if result[e_id] != 0:
                continue
            # Pick a color not used at u or v
            color = None
            for c in available:
                if c not in used[v + nL]:
                    color = c
                    break
            if color is None:
                # This shouldn't happen given the theory, but just in case
                for c in range(1, max_degree + 1):
                    if c not in used[u] and c not in used[v + nL]:
                        color = c
                        break
            result[e_id] = color
            used[u].add(color)
            used[v + nL].add(color)
            available.discard(color)
    
    print("YES")
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()